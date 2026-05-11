import fs from 'fs';
import path from 'path';

/* =========================
   AFFILIATE CONFIG (LOCKED)
========================= */

const AFFILIATE_ID = "wloofjbvk5mp";
const AFFILIATE_LINK = `https://get.junglescout.com/${AFFILIATE_ID}`;

/* =========================
   CROSS LINK SYSTEM
========================= */

function injectCrossLinks(content, language) {

  const siteBase =
    `https://yourdomain.com/${language}`;

  const crossLinks = [
    {
      keyword: 'Amazon FBA',
      url: `${siteBase}/best-amazon-fba-products-2026.html`
    },

    {
      keyword: 'JungleScout',
      url: AFFILIATE_LINK // ALWAYS affiliate protected
    },

    {
      keyword: 'FBA product research',
      url: `${siteBase}/fba-product-research-guide.html`
    }
  ];

  crossLinks.forEach(link => {

    // Avoid breaking existing HTML links
    const regex = new RegExp(
      `(?<!href=["'])\\b${link.keyword}\\b`,
      'gi'
    );

    content = content.replace(regex, (match) => {

      // Prevent double linking
      if (match.includes("<a")) return match;

      return `<a href="${link.url}" target="_blank" rel="noopener">
                ${match}
              </a>`;
    });
  });

  return content;
}

/* =========================
   META TAG ENGINE (FIXED)
========================= */

function injectMetaTags(html, title) {

  const slug =
    title.toLowerCase()
      .replace(/[^a-z0-9]+/g, "-");

  const metaTags = `
<meta name="description"
      content="${title} - Amazon FBA & JungleScout Guide">

<meta name="keywords"
      content="${title}, Amazon FBA, JungleScout, ecommerce">

<meta property="og:title"
      content="${title}">

<meta property="og:description"
      content="${title} - Learn Amazon FBA with JungleScout">

<meta property="og:url"
      content="https://yourdomain.com/${slug}.html">

<meta property="og:type"
      content="article">

<meta name="robots"
      content="index, follow">
`;

  // Prevent duplicate injection
  if (html.includes('og:title')) {
    return html;
  }

  return html.replace(
    '</head>',
    `${metaTags}\n</head>`
  );
}

/* =========================
   AFFILIATE SAFETY CHECK
========================= */

function enforceAffiliate(content) {

  // Replace any non-affiliate JungleScout links
  content = content.replace(
    /https:\/\/(www\.)?junglescout\.com/gi,
    AFFILIATE_LINK
  );

  // Ensure it always exists
  if (!content.includes(AFFILIATE_LINK)) {
    content += `

<hr>

<h2>🚀 Recommended Tool</h2>

<p>
JungleScout helps Amazon sellers find profitable products,
analyze competition, and scale faster.
</p>

<a href="${AFFILIATE_LINK}" target="_blank" rel="sponsored noopener">
👉 Try JungleScout
</a>
`;
  }

  return content;
}

/* =========================
   ARTICLE UPDATER
========================= */

function updateArticle(filePath, language) {

  let html =
    fs.readFileSync(filePath, 'utf8');

  const titleMatch =
    html.match(/<title>(.*?)<\/title>/);

  const title =
    titleMatch ? titleMatch[1] : 'Untitled';

  // Apply updates in correct order
  html = injectCrossLinks(html, language);
  html = injectMetaTags(html, title);
  html = enforceAffiliate(html);

  fs.writeFileSync(filePath, html);

  console.log(
    `✅ Updated SEO + links + affiliate: ${filePath}`
  );
}

/* =========================
   PROCESS ALL FILES
========================= */

function updateAllArticles() {

  const languages =
    ['en', 'es', 'fr', 'de', 'it'];

  languages.forEach(language => {

    const dirPath =
      path.join(__dirname, 'posts', language);

    if (!fs.existsSync(dirPath)) return;

    fs.readdirSync(dirPath).forEach(file => {

      const filePath =
        path.join(dirPath, file);

      updateArticle(filePath, language);
    });
  });
}

/* =========================
   RUN
========================= */

updateAllArticles();
