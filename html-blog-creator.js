import fs from "fs";
import path from "path";

/* =========================
   CONFIG
========================= */

const OUTPUT_DIR = "./generated-posts";

const AFFILIATE_ID = "wloofjbvk5mp";
const AFFILIATE_URL = `https://get.junglescout.com/${AFFILIATE_ID}`;

const BRAND = "JungleScout";

/* =========================
   INIT
========================= */

if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR);
}

/* =========================
   SLUGIFY
========================= */

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/(^-|-$)+/g, "");
}

/* =========================
   AFFILIATE ENFORCER
========================= */

function enforceAffiliate(content) {

  // Replace any non-affiliate JungleScout links
  content = content.replace(
    /https:\/\/(www\.)?junglescout\.com/gi,
    AFFILIATE_URL
  );

  // Ensure affiliate always exists
  if (!content.includes(AFFILIATE_URL)) {
    content += `
      <div class="cta">
        <h3>🚀 Recommended Tool</h3>
        <p>
          JungleScout helps Amazon sellers find winning products,
          analyze competition, and scale faster.
        </p>
        <a href="${AFFILIATE_URL}"
           target="_blank"
           rel="sponsored noopener">
           👉 Try JungleScout
        </a>
      </div>
    `;
  }

  return content;
}

/* =========================
   HTML TEMPLATE
========================= */

function buildHTML({
  title,
  content,
  description,
  affiliateUrl
}) {

  const safeContent =
    enforceAffiliate(content);

  return `
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>${title}</title>

  <meta name="description" content="${description}" />
  <meta name="robots" content="index, follow" />

  <!-- Open Graph -->
  <meta property="og:title" content="${title}" />
  <meta property="og:description" content="${description}" />
  <meta property="og:type" content="article" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="${title}" />
  <meta name="twitter:description" content="${description}" />

  <style>

    body {
      font-family: Arial, sans-serif;
      max-width: 900px;
      margin: auto;
      padding: 40px;
      line-height: 1.7;
      color: #222;
    }

    h1 { font-size: 32px; }
    h2 { margin-top: 30px; }

    a { color: #0073ff; }

    .cta {
      margin: 30px 0;
      padding: 20px;
      background: #f5f5f5;
      border-left: 5px solid #0073ff;
    }

    .affiliate-btn {
      display: inline-block;
      margin-top: 10px;
      padding: 12px 18px;
      background: #f59e0b;
      color: #000;
      text-decoration: none;
      font-weight: bold;
      border-radius: 6px;
    }

  </style>

</head>

<body>

  <article>

    <h1>${title}</h1>

    <p><strong>${description}</strong></p>

    <div>
      ${safeContent}
    </div>

    <div class="cta">
      <h3>🚀 JungleScout Recommended Tool</h3>

      <p>
        Use JungleScout to discover profitable Amazon products,
        analyze competitors, and scale your store efficiently.
      </p>

      <a class="affiliate-btn"
         href="${affiliateUrl}"
         target="_blank"
         rel="sponsored noopener">
         Try JungleScout Now
      </a>
    </div>

    <hr />

    <p style="font-size:12px;color:#777;">
      Affiliate disclosure: This page contains affiliate links.
    </p>

  </article>

</body>
</html>
`;
}

/* =========================
   MAIN FUNCTION
========================= */

export function createBlogPage({
  title,
  description,
  content,
  affiliateUrl
}) {

  const slug =
    slugify(title);

  const filePath =
    path.join(OUTPUT_DIR, `${slug}.html`);

  const html =
    buildHTML({
      title,
      description,
      content,
      affiliateUrl: affiliateUrl || AFFILIATE_URL
    });

  fs.writeFileSync(filePath, html, "utf-8");

  console.log("✅ Created:", filePath);

  return filePath;
}

/* =========================
   EXAMPLE
========================= */

createBlogPage({
  title: "How to Build a Profitable Amazon FBA Store",
  description: "A complete beginner guide to starting Amazon FBA in 2026.",
  content: `
    <p>Amazon FBA allows sellers to leverage Amazon's logistics network.</p>

    <h2>Step 1: Product Research</h2>
    <p>Use data-driven tools to find winning products.</p>

    <h2>Step 2: Supplier Sourcing</h2>
    <p>Work with reliable manufacturers for quality control.</p>

    <h2>Step 3: Launch Strategy</h2>
    <p>Optimize listings and run PPC campaigns for visibility.</p>
  `,
  affiliateUrl: AFFILIATE_URL
});
