import os
import multiprocessing as mp
import itertools
import time
import subprocess
from datetime import datetime

# =========================
# CONFIG
# =========================

DOMAIN = "https://brightlane.github.io/Junglescout.com"
AFFILIATE = "https://get.junglescout.com/wloofjbvk5mp"

OUTPUT_DIR = "site"
SITEMAP_DIR = "site/sitemaps"

PAGES_PER_RUN = 100000
WORKERS = 8

keywords = [
    "Amazon FBA product research",
    "best Amazon FBA tools",
    "low competition Amazon products",
    "JungleScout guide",
    "how to find winning Amazon products",
]

locations = [
    "USA", "UK", "Canada", "Germany",
    "India", "Australia", "Global"
]

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SITEMAP_DIR, exist_ok=True)

# =========================
# PAGE GENERATOR
# =========================

def generate_page(keyword, location, i):
    slug = f"{keyword}-{location}-{i}".lower().replace(" ", "-")

    url = f"{DOMAIN}/seo/{slug}.html"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>{keyword} {location}</title>

<meta name="description" content="{keyword} guide for {location}">
<meta name="robots" content="index, follow">

<meta name="geo.region" content="{location}">
<meta name="content-language" content="en">

</head>

<body style="font-family:Arial;max-width:900px;margin:auto;padding:40px;">

<h1>{keyword} ({location})</h1>

<p>
High-level Amazon FBA strategy for {location}.
</p>

<h2>Recommended Tool</h2>

<a href="{AFFILIATE}" target="_blank" rel="sponsored">
JungleScout Affiliate Tool
</a>

<p>
Global scaling strategy applies across all regions.
</p>

</body>
</html>
"""

    return slug, url, html

# =========================
# SAVE FILE
# =========================

def save_file(slug, html):
    path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path

# =========================
# SITEMAP SYSTEM
# =========================

def write_sitemap(urls, index):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset>\n'

    for u in urls:
        xml += f"<url><loc>{u}</loc></url>\n"

    xml += "</urlset>"

    path = os.path.join(SITEMAP_DIR, f"sitemap-{index}.xml")
    with open(path, "w") as f:
        f.write(xml)

# =========================
# INDEXING PING
# =========================

def ping(url):
    try:
        subprocess.run([
            "curl",
            f"https://www.google.com/ping?sitemap={url}"
        ], stdout=subprocess.DEVNULL)

        subprocess.run([
            "curl",
            f"https://www.bing.com/ping?sitemap={url}"
        ], stdout=subprocess.DEVNULL)

    except:
        pass

# =========================
# WORKER
# =========================

def worker(task):
    i, keyword, location = task

    slug, url, html = generate_page(keyword, location, i)

    save_file(slug, html)

    return url

# =========================
# SWARM RUNNER
# =========================

def run_swarm():

    print("🚀 SEO SWARM STARTED")

    pool = mp.Pool(WORKERS)

    tasks = []

    for i in range(PAGES_PER_RUN):
        keyword = keywords[i % len(keywords)]
        location = locations[i % len(locations)]
        tasks.append((i, keyword, location))

    urls = []

    # multiprocessing map
    for result in pool.imap(worker, tasks):
        urls.append(result)

    pool.close()
    pool.join()

    # =========================
    # SITEMAP SPLIT (50k)
    # =========================

    print("🗺 Generating sitemaps...")

    chunks = [urls[i:i+50000] for i in range(0, len(urls), 50000)]

    for idx, chunk in enumerate(chunks):
        write_sitemap(chunk, idx+1)

    # =========================
    # PING INDEXING
    # =========================

    print("📡 Pinging search engines...")

    for u in urls[:100]:  # avoid spam limits
        ping(u)

    # =========================
    # AUTO GIT DEPLOY
    # =========================

    print("🚀 Deploying to GitHub...")

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run([
            "git", "commit", "-m",
            f"SEO update {datetime.now()}"
        ])
        subprocess.run(["git", "push"], check=True)
    except:
        print("Git deploy skipped (no changes or auth issue)")

    print("✅ SWARM COMPLETE")

# =========================
# RUN DAILY LOOP
# =========================

if __name__ == "__main__":
    run_swarm()
