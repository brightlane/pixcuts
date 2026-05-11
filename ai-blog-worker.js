import OpenAI from "openai";
import fs from "fs";
import path from "path";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

/* =========================
   AFFILIATE CONFIG (LOCKED)
========================= */

const AFFILIATE_ID = "wloofjbvk5mp";
const AFFILIATE_LINK = `https://get.junglescout.com/${AFFILIATE_ID}`;

const BRAND_NAME = "JungleScout";

/* =========================
   SETUP
========================= */

if (!fs.existsSync("./posts")) {
  fs.mkdirSync("./posts");
}

/* =========================
   KEYWORDS
========================= */

const keywords = [
  "best Amazon FBA products 2026",
  "how to find winning Amazon products",
  "JungleScout product research guide",
  "Amazon FBA beginner strategy",
  "low competition Amazon niches",
  "how to scale Amazon FBA business",
  "product research tools for Amazon sellers",
  "how to start Amazon FBA with no experience"
];

function pickKeyword() {
  return keywords[Math.floor(Math.random() * keywords.length)];
}

/* =========================
   AFFILIATE ENFORCER
========================= */

function enforceAffiliate(content) {
  // Replace any generic JungleScout links with affiliate
  content = content.replace(/https:\/\/(www\.)?junglescout\.com/gi, AFFILIATE_LINK);

  // Always ensure affiliate link exists
  if (!content.includes(AFFILIATE_LINK)) {
    content += `

---

## 🚀 Recommended Tool

If you're serious about Amazon FBA, you should use JungleScout:

👉 ${AFFILIATE_LINK}

It helps you:
- Find winning products
- Analyze competition
- Estimate sales
- Validate niches before investing
`;
  }

  return content;
}

/* =========================
   AI ARTICLE GENERATION
========================= */

async function generateArticle(keyword) {
  const prompt = `
Write a HIGH QUALITY SEO blog article about Amazon FBA.

Topic: ${keyword}

Rules:
- 1500–2500 words
- Clear headings
- Natural human tone
- No keyword stuffing
- Beginner friendly but insightful

STRUCTURE:
1. Introduction
2. Problem breakdown
3. Step-by-step strategy
4. Tools section (MUST mention JungleScout)
5. Common mistakes
6. Final advice

IMPORTANT RULES:
- Include JungleScout naturally as the #1 tool recommendation
- Include this affiliate link at least once:
${AFFILIATE_LINK}
`;

  const res = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: prompt }],
  });

  let article = res.choices[0].message.content;

  // FORCE AFFILIATE CONSISTENCY
  article = enforceAffiliate(article);

  return article;
}

/* =========================
   HTML TEMPLATE
========================= */

function wrapHTML(title, content) {
  return `
<!DOCTYPE html>
<html>
<head>
  <title>${title}</title>
  <meta name="description" content="${title}">
  <meta name="robots" content="index, follow">
</head>

<body style="font-family:Arial;max-width:850px;margin:auto;padding:20px;background:#0b1220;color:#fff;">

  <h1>${title}</h1>

  <article style="line-height:1.7;background:#111827;padding:20px;border-radius:10px;">
    ${content.replace(/\n/g, "<br>")}
  </article>

  <section style="margin-top:30px;padding:20px;background:#1e293b;border-radius:10px;">
    <h2>🚀 Start Using JungleScout</h2>

    <p>
      JungleScout is the leading Amazon FBA research tool for finding profitable products,
      analyzing competitors, and scaling ecommerce businesses.
    </p>

    <a href="${AFFILIATE_LINK}"
       target="_blank"
       style="display:inline-block;margin-top:10px;padding:12px 18px;background:#f59e0b;color:#000;font-weight:bold;text-decoration:none;border-radius:8px;">
       Try JungleScout Now
    </a>
  </section>

</body>
</html>
`;
}

/* =========================
   SAVE ARTICLE
========================= */

function saveArticle(title, content) {
  const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-");
  const filePath = path.join("./posts", `${slug}.html`);

  const html = wrapHTML(title, content);

  fs.writeFileSync(filePath, html);
  console.log("Saved:", filePath);
}

/* =========================
   SAFE WAIT
========================= */

function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/* =========================
   WORKER LOOP
========================= */

async function startWorker() {
  console.log("🚀 AI Blog Worker Started...");

  while (true) {
    try {
      const keyword = pickKeyword();

      console.log("🧠 Generating:", keyword);

      const article = await generateArticle(keyword);

      saveArticle(keyword, article);

      console.log("✅ Done:", keyword);

      // 1 post per hour
      await wait(60 * 60 * 1000);

    } catch (err) {
      console.error("❌ Error:", err.message);

      await wait(5 * 60 * 1000);
    }
  }
}

startWorker();
