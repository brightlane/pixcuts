import OpenAI from 'openai';
import { Translate } from '@google-cloud/translate';
import fs from 'fs';
import path from 'path';
import { google } from 'googleapis';
import dotenv from 'dotenv';

dotenv.config();

/* =========================
   CONFIG (LOCKED AFFILIATE)
========================= */

const AFFILIATE_ID = "wloofjbvk5mp";
const AFFILIATE_LINK = `https://get.junglescout.com/${AFFILIATE_ID}`;

const BRAND_NAME = "JungleScout";

/* FIX for ES MODULES */
const __dirname = path.resolve();

/* =========================
   INIT
========================= */

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

const translate = new Translate({
  key: process.env.GOOGLE_API_KEY
});

const indexer = google.indexing('v3');

/* =========================
   GOOGLE INDEXING
========================= */

async function notifyGoogleOfNewContent(url) {
  const auth = new google.auth.GoogleAuth({
    scopes: ['https://www.googleapis.com/auth/indexing'],
  });

  const authClient = await auth.getClient();
  google.options({ auth: authClient });

  await indexer.urlNotifications.publish({
    requestBody: {
      url,
      type: 'URL_UPDATED',
    },
  });

  console.log('Google Indexing API notified:', url);
}

/* =========================
   AFFILIATE ENFORCER
========================= */

function enforceAffiliate(content) {

  // Replace any fake/non-affiliate links
  content = content.replace(
    /https:\/\/(www\.)?junglescout\.com/gi,
    AFFILIATE_LINK
  );

  // Guarantee presence
  if (!content.includes(AFFILIATE_LINK)) {
    content += `

---

## 🚀 Recommended Tool: JungleScout

Amazon sellers use JungleScout to:
- Find winning products
- Analyze competition
- Validate niches
- Scale faster

👉 ${AFFILIATE_LINK}
`;
  }

  return content;
}

/* =========================
   ARTICLE GENERATION
========================= */

async function generateArticle(keyword, language = 'en') {

  const prompt = `
Write a high-quality SEO blog article about "${keyword}".

Structure:
- Introduction
- Problem explanation
- Step-by-step guide
- Tools section (must include JungleScout)
- Mistakes to avoid
- Conclusion

IMPORTANT:
- Include JungleScout naturally as the main tool
- Include this affiliate link ONCE:
${AFFILIATE_LINK}
`;

  const res = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: prompt }],
  });

  let articleContent = res.choices[0].message.content;

  // ENFORCE AFFILIATE BEFORE TRANSLATION
  articleContent = enforceAffiliate(articleContent);

  // Translate if needed
  if (language !== 'en') {
    const [translation] = await translate.translate(articleContent, language);
    articleContent = translation;

    // RE-ENFORCE after translation (important!)
    articleContent = enforceAffiliate(articleContent);
  }

  return articleContent;
}

/* =========================
   SAVE ARTICLE
========================= */

async function saveArticle(title, content, language = 'en') {

  const slug =
    title.toLowerCase().replace(/[^a-z0-9]+/g, '-');

  const dirPath =
    path.join(__dirname, 'posts', language);

  const filePath =
    path.join(dirPath, `${slug}.html`);

  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }

  const html = `
<!DOCTYPE html>
<html lang="${language}">
<head>

  <title>${title}</title>
  <meta name="description" content="${title}">
  <meta name="keywords" content="${title}, JungleScout, Amazon FBA">

</head>

<body style="font-family:Arial;max-width:800px;margin:auto;padding:20px;">

  <article>
    <h1>${title}</h1>

    <div>
      ${content.replace(/\n/g, '<br>')}
    </div>

    <hr>

    <section style="margin-top:30px;padding:20px;background:#f3f3f3;border-radius:10px;">
      <h2>🚀 Try JungleScout</h2>

      <p>
        JungleScout helps Amazon sellers discover profitable products,
        validate demand, and scale ecommerce businesses.
      </p>

      <a href="${AFFILIATE_LINK}" target="_blank">
        👉 Start with JungleScout
      </a>

    </section>

  </article>

</body>
</html>
`;

  fs.writeFileSync(filePath, html);

  console.log(`Article saved: ${filePath}`);

  const articleUrl =
    `https://yourdomain.com/posts/${language}/${slug}.html`;

  await notifyGoogleOfNewContent(articleUrl);

  return filePath;
}

/* =========================
   GENERATOR LOOP
========================= */

async function runGenerator() {

  const languages = ['en', 'es', 'fr', 'de', 'it'];

  const keywords = [
    "Best Amazon FBA tools for 2026",
    "How to find winning Amazon products",
    "JungleScout vs Helium 10",
    "Product research guide for Amazon FBA",
    "How to scale your Amazon FBA business"
  ];

  const keyword =
    keywords[Math.floor(Math.random() * keywords.length)];

  const language =
    languages[Math.floor(Math.random() * languages.length)];

  const article =
    await generateArticle(keyword, language);

  const file =
    await saveArticle(keyword, article, language);

  console.log("Generated and saved:", file);
}

/* =========================
   AUTO RUN
========================= */

setInterval(runGenerator, 3600000); // 1 hour
