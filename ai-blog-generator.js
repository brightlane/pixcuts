/*
========================================================
 AI BLOG GENERATOR — ENHANCED VERSION
 JungleScout Affiliate SEO Automation Engine
========================================================
*/

const OpenAI = require("openai");
const fs = require("fs");
const path = require("path");

/* ========================================
   CONFIG
======================================== */

const AFFILIATE_ID = "wloofjbvk5mp";

const AFFILIATE_LINK =
  `https://get.junglescout.com/${AFFILIATE_ID}`;

const REVIEW_LINK =
  "https://brightlane.github.io/Junglescout.com/#review";

const SITE_URL =
  "https://brightlane.github.io/Junglescout.com";

const BRAND_NAME =
  "JungleScout Growth Hub";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

/* ========================================
   KEYWORDS
======================================== */

const keywords = [
  "JungleScout Amazon FBA guide",
  "Amazon FBA product research",
  "Best Amazon FBA tools",
  "How to use JungleScout",
  "Product research Amazon FBA",
  "Amazon keyword research tools",
  "Amazon seller software",
  "Best JungleScout alternatives",
  "How to find winning Amazon products",
  "Low competition Amazon niches",
  "Amazon FBA for beginners",
  "Private label product research",
  "Amazon product validation",
  "Amazon SEO optimization",
  "Amazon listing optimization",
  "Amazon sales estimator",
  "Amazon niche finder",
  "How to scale Amazon FBA",
  "JungleScout keyword scout",
  "Best ecommerce research tools"
];

/* ========================================
   INTERNAL LINKING ENGINE
======================================== */

function generateInternalLinks() {
  return `
    <section class="internal-links">
      <h2>Recommended Resources</h2>

      <ul>
        <li>
          <a href="${REVIEW_LINK}">
            Full JungleScout Review
          </a>
        </li>

        <li>
          <a href="${AFFILIATE_LINK}" rel="sponsored noopener" target="_blank">
            Try JungleScout
          </a>
        </li>

        <li>
          <a href="${SITE_URL}">
            Amazon FBA Strategy Hub
          </a>
        </li>
      </ul>
    </section>
  `;
}

/* ========================================
   CTA ENGINE
======================================== */

function generateCTA() {
  return `
    <section class="cta-box">
      <h2>🚀 Start Growing with JungleScout</h2>

      <p>
        JungleScout helps Amazon sellers discover profitable products,
        validate demand, estimate revenue, analyze competitors,
        and scale ecommerce brands using real marketplace data.
      </p>

      <p>
        Whether you're a beginner or advanced seller,
        using professional research tools can dramatically
        reduce risk and improve profitability.
      </p>

      <a
        href="${AFFILIATE_LINK}"
        target="_blank"
        rel="noopener sponsored"
        class="affiliate-button"
      >
        Try JungleScout Today
      </a>

      <br><br>

      <a
        href="${REVIEW_LINK}"
        target="_blank"
        rel="noopener"
      >
        Read Full JungleScout Review →
      </a>
    </section>
  `;
}

/* ========================================
   AFFILIATE LINK ENFORCER
======================================== */

function enforceAffiliateLinks(content) {

  // Replace all raw JungleScout URLs
  content = content.replace(
    /https:\/\/www\.junglescout\.com/gi,
    AFFILIATE_LINK
  );

  content = content.replace(
    /https:\/\/junglescout\.com/gi,
    AFFILIATE_LINK
  );

  // Ensure affiliate link exists multiple times
  if (!content.includes(AFFILIATE_LINK)) {
    content += `

    <p>
      Recommended Tool:
      <a href="${AFFILIATE_LINK}" target="_blank" rel="sponsored noopener">
        JungleScout
      </a>
    </p>
    `;
  }

  return content;
}

/* ========================================
   SEO META TAGS
======================================== */

function generateMetaTags(keyword) {

  const title =
    `${keyword} | JungleScout Amazon FBA Guide`;

  const description =
    `Learn ${keyword} using advanced Amazon FBA strategies, JungleScout tools, keyword research, product validation techniques, and ecommerce scaling systems.`;

  const metaKeywords =
    `${keyword}, JungleScout, Amazon FBA, ecommerce, Amazon SEO, product research, private label, keyword research`;

  return {
    title,
    description,
    metaKeywords,
  };
}

/* ========================================
   ARTICLE GENERATION
======================================== */

async function generateArticle(keyword) {

  const prompt = `
You are an expert Amazon FBA SEO writer.

Write a premium long-form blog article about:
"${keyword}"

Requirements:

- 2000 to 3500 words
- Highly informative
- SEO optimized naturally
- Human sounding
- Professional formatting
- Include detailed sections
- Include examples
- Include FAQs
- Use markdown-style headings

STRUCTURE:

1. Introduction
2. Why this matters
3. Common problems sellers face
4. Step-by-step strategy
5. Best tools for success
6. Why JungleScout is valuable
7. Mistakes to avoid
8. Expert tips
9. FAQ section
10. Final conclusion

IMPORTANT:

- Mention JungleScout naturally throughout the article.
- Include this affiliate link naturally multiple times:
${AFFILIATE_LINK}

- Never use a non-affiliate JungleScout link.
- Encourage readers to explore:
${REVIEW_LINK}

- Write for BOTH beginners and advanced Amazon sellers.
- Avoid keyword stuffing.
- Include practical ecommerce advice.
- Use engaging formatting.
`;

  try {

    const response =
      await openai.chat.completions.create({

        model: "gpt-4.1",

        temperature: 0.8,

        messages: [
          {
            role: "system",
            content:
              "You are a world-class Amazon FBA SEO content writer.",
          },

          {
            role: "user",
            content: prompt,
          },
        ],
      });

    let article =
      response.choices[0].message.content;

    article = enforceAffiliateLinks(article);

    return article;

  } catch (error) {

    console.error("Error generating article:", error);

    throw new Error("Error generating article.");
  }
}

/* ========================================
   HTML TEMPLATE
======================================== */

function generateHTMLTemplate(
  title,
  content,
  metaTags
) {

  return `
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8" />

<meta name="viewport"
      content="width=device-width, initial-scale=1.0" />

<title>${metaTags.title}</title>

<meta name="description"
      content="${metaTags.description}" />

<meta name="keywords"
      content="${metaTags.metaKeywords}" />

<meta name="robots"
      content="index, follow" />

<meta property="og:title"
      content="${metaTags.title}" />

<meta property="og:description"
      content="${metaTags.description}" />

<meta property="og:type"
      content="article" />

<meta property="og:url"
      content="${SITE_URL}" />

<link rel="canonical"
      href="${SITE_URL}" />

<style>

body{
  margin:0;
  padding:40px;
  background:#0b1220;
  color:#ffffff;
  font-family:Arial,sans-serif;
  line-height:1.8;
  max-width:900px;
  margin:auto;
}

h1,h2,h3{
  color:#fbbf24;
}

a{
  color:#f59e0b;
}

article{
  background:#111827;
  padding:40px;
  border-radius:14px;
}

.cta-box{
  margin-top:40px;
  padding:30px;
  background:#1e293b;
  border-radius:12px;
}

.affiliate-button{
  display:inline-block;
  margin-top:20px;
  padding:14px 24px;
  background:#f59e0b;
  color:#000;
  text-decoration:none;
  font-weight:bold;
  border-radius:8px;
}

.internal-links{
  margin-top:50px;
}

</style>

</head>

<body>

<article>

<h1>${title}</h1>

${content.replace(/\n/g, "<br>")}

${generateCTA()}

${generateInternalLinks()}

</article>

</body>
</html>
`;
}

/* ========================================
   SAVE ARTICLE
======================================== */

async function saveArticle(
  title,
  content,
  metaTags
) {

  const slug =
    title
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-|-$/g, "");

  const postsDir =
    path.join(__dirname, "posts");

  if (!fs.existsSync(postsDir)) {
    fs.mkdirSync(postsDir);
  }

  const filePath =
    path.join(postsDir, `${slug}.html`);

  const htmlContent =
    generateHTMLTemplate(
      title,
      content,
      metaTags
    );

  fs.writeFileSync(
    filePath,
    htmlContent,
    "utf8"
  );

  return filePath;
}

/* ========================================
   GENERATE ALL ARTICLES
======================================== */

async function generateAndSaveArticleForAllKeywords() {

  try {

    for (const keyword of keywords) {

      console.log(
        `Generating article for: ${keyword}`
      );

      const article =
        await generateArticle(keyword);

      const metaTags =
        generateMetaTags(keyword);

      const filePath =
        await saveArticle(
          keyword,
          article,
          metaTags
        );

      console.log(
        `✅ Article saved: ${filePath}`
      );
    }

  } catch (error) {

    console.error(
      "Error generating articles:",
      error
    );
  }
}

/* ========================================
   EXPORTS
======================================== */

module.exports = {
  generateArticle,
  saveArticle,
  generateMetaTags,
  generateAndSaveArticleForAllKeywords,
  AFFILIATE_LINK,
  REVIEW_LINK,
};

/* ========================================
   AUTO RUN (OPTIONAL)
======================================== */

// Uncomment below if you want automatic execution
// generateAndSaveArticleForAllKeywords();
