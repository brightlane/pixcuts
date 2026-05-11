const fs = require('fs');
const axios = require('axios');
const OpenAI = require("openai");
const Twitter = require('twitter');

/* =========================
   CONFIG
========================= */

const AFFILIATE_ID = "wloofjbvk5mp";
const AFFILIATE_LINK = `https://get.junglescout.com/${AFFILIATE_ID}`;

const REVIEW_LINK =
  "https://brightlane.github.io/Junglescout.com/#review";

/* =========================
   OPENAI SETUP
========================= */

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

/* =========================
   TWITTER SETUP
========================= */

const twitterClient = new Twitter({
  consumer_key: process.env.TWITTER_CONSUMER_KEY,
  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
  access_token_key: process.env.TWITTER_ACCESS_TOKEN,
  access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET
});

/* =========================
   AFFILIATE ENFORCER
========================= */

function enforceAffiliate(content) {

  // Replace any non-affiliate JungleScout links
  content = content.replace(
    /https:\/\/(www\.)?junglescout\.com/gi,
    AFFILIATE_LINK
  );

  // Guarantee presence
  if (!content.includes(AFFILIATE_LINK)) {
    content += `

---

## 🚀 Recommended Tool: JungleScout

Start using professional Amazon FBA research tools:

👉 ${AFFILIATE_LINK}

Learn more here:
👉 ${REVIEW_LINK}
`;
  }

  return content;
}

/* =========================
   ARTICLE GENERATION
========================= */

async function generateArticle(
  keyword = "Amazon FBA product research",
  language = "en"
) {

  const prompt = `
You are an expert SEO content writer specializing in Amazon FBA.

Write a HIGH QUALITY blog article.

Topic: ${keyword}

Requirements:
- 1500–2500 words
- SEO optimized but natural
- Human tone
- Structured headings

Sections:
1. Introduction
2. Problem explanation
3. Step-by-step guide
4. Tools section (MUST include JungleScout)
5. Mistakes to avoid
6. Conclusion

AFFILIATE RULES:
- Mention JungleScout as a recommended tool
- Include this link at least ONCE:
${AFFILIATE_LINK}

- Encourage readers to explore:
${REVIEW_LINK}
`;

  const res = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: prompt }],
  });

  let articleContent = res.choices[0].message.content;

  // FORCE AFFILIATE CONSISTENCY
  articleContent = enforceAffiliate(articleContent);

  // Translate if needed
  if (language !== "en") {
    articleContent = await translateContent(articleContent, language);
  }

  return articleContent;
}

/* =========================
   TRANSLATION
========================= */

async function translateContent(text, targetLanguage) {
  const response = await axios.post(
    `https://translation.googleapis.com/language/translate/v2?key=${process.env.GOOGLE_API_KEY}`,
    {
      q: text,
      target: targetLanguage,
    }
  );

  return response.data.data.translations[0].translatedText;
}

/* =========================
   HTML SAVER
========================= */

async function saveArticle(title, content, language) {

  const slug =
    title.toLowerCase()
      .replace(/[^a-z0-9]+/g, "-");

  const dir = `./posts/${language}`;

  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }

  const filePath =
    `${dir}/${slug}.html`;

  const html = `
<html lang="${language}">
<head>

  <title>${title}</title>
  <meta name="description" content="${title}">
  <meta name="robots" content="index, follow">

</head>

<body style="font-family:Arial;max-width:800px;margin:auto;padding:20px;">

  <h1>${title}</h1>

  <article>
    ${content.replace(/\n/g, "<br>")}
  </article>

  <hr>

  <section>
    <h2>🚀 Try JungleScout</h2>

    <p>
      Amazon sellers use JungleScout to find profitable products,
      validate niches, and scale faster.
    </p>

    <a href="${AFFILIATE_LINK}" target="_blank">
      👉 Start with JungleScout
    </a>

    <br><br>

    <a href="${REVIEW_LINK}" target="_blank">
      Read Full Review →
    </a>
  </section>

</body>
</html>
`;

  await fs.promises.writeFile(filePath, html);

  return filePath;
}

/* =========================
   GOOGLE INDEXING
========================= */

async function submitToGoogleIndexingAPI(url) {
  const response = await axios.post(
    'https://indexing.googleapis.com/v3/urlNotifications:publish',
    {
      url: url,
      type: 'URL_UPDATED'
    },
    {
      headers: {
        'Authorization': `Bearer ${process.env.GOOGLE_API_KEY}`
      }
    }
  );

  console.log("Submitted to Google:", response.data);
}

/* =========================
   TWITTER POSTING
========================= */

async function postToTwitter(content) {
  try {

    const tweet =
      `${content}\n\nTry JungleScout 👉 ${AFFILIATE_LINK}`;

    await twitterClient.post('statuses/update', {
      status: tweet.slice(0, 275) // safe limit
    });

    console.log("Posted to Twitter successfully!");

  } catch (error) {
    console.error("Error posting to Twitter:", error);
  }
}

/* =========================
   MAIN RUNNER
========================= */

async function runGenerator() {

  const keywords = [
    "best Amazon FBA products 2026",
    "how to find winning products on Amazon",
    "JungleScout product research guide",
    "Amazon FBA beginner strategy",
    "low competition Amazon niches"
  ];

  const languages = ['en', 'es', 'fr', 'de', 'pt'];

  const keyword =
    keywords[Math.floor(Math.random() * keywords.length)];

  const language =
    languages[Math.floor(Math.random() * languages.length)];

  const article =
    await generateArticle(keyword, language);

  const path =
    await saveArticle(keyword, article, language);

  console.log("Generated article at:", path);

  // Google indexing
  await submitToGoogleIndexingAPI(path);

  // Twitter promotion
  const message =
    `New blog: ${keyword} | SEO Amazon FBA guide + tools`;

  await postToTwitter(message);
}

/* =========================
   START
========================= */

runGenerator();
