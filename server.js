import express from 'express';
import path from 'path';

import {
  generateArticle,
  saveArticle
} from './ai-blog-generator.js';

const app = express();
const port = process.env.PORT || 3000;

const __dirname = path.resolve();

/* =========================
   MIDDLEWARE
========================= */

app.use(express.json());

/* =========================
   BASIC RATE LIMIT (SAFE GUARD)
========================= */

let lastRequestTime = 0;

function rateLimit(req, res, next) {
  const now = Date.now();

  // 10 sec cooldown between article generations
  if (now - lastRequestTime < 10000) {
    return res.status(429).send(
      "Too many requests. Please wait a few seconds."
    );
  }

  lastRequestTime = now;
  next();
}

/* =========================
   HOMEPAGE
========================= */

app.get('/', (req, res) => {
  res.send(`
    <h1>🚀 Content Generator System</h1>
    <p>Generate SEO Amazon FBA articles automatically.</p>
    <p>Use: /generate-article?keyword=your-topic</p>
  `);
});

/* =========================
   ARTICLE GENERATOR ROUTE
========================= */

app.get('/generate-article', rateLimit, async (req, res) => {

  try {

    const keyword =
      req.query.keyword || "Amazon FBA tips";

    console.log("🧠 Generating article:", keyword);

    const article =
      await generateArticle(keyword);

    const filePath =
      await saveArticle(keyword, article);

    console.log("✅ Saved:", filePath);

    // Convert file path into accessible URL
    const fileUrl =
      `/posts/${path.basename(filePath)}`;

    res.send(`
      <h1>✅ Article Generated</h1>

      <p><strong>Keyword:</strong> ${keyword}</p>

      <p><strong>Saved File:</strong> ${filePath}</p>

      <a href="${fileUrl}" target="_blank">
        👉 View Article
      </a>

      <br><br>

      <a href="/">
        ⬅ Back Home
      </a>
    `);

  } catch (error) {

    console.error("❌ Error generating article:", error);

    res.status(500).send(`
      <h1>Error generating article</h1>
      <p>Please try again later.</p>
    `);
  }
});

/* =========================
   STATIC POSTS (SEO PAGES)
========================= */

app.use(
  '/posts',
  express.static(path.join(__dirname, 'posts'), {
    extensions: ['html']
  })
);

/* =========================
   HEALTH CHECK (SAAS READY)
========================= */

app.get('/health', (req, res) => {
  res.json({
    status: "ok",
    uptime: process.uptime()
  });
});

/* =========================
   START SERVER
========================= */

app.listen(port, () => {
  console.log(
    `🚀 Server running at http://localhost:${port}`
  );
});
