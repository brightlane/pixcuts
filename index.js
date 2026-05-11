import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();
app.use(express.json());

/* =========================
   CONFIG (AFFILIATE LOCK)
========================= */

const AFFILIATE_ID = "wloofjbvk5mp";
const AFFILIATE_LINK = `https://get.junglescout.com/${AFFILIATE_ID}`;

const __dirname = path.resolve();

/* =========================
   FILE PATHS
========================= */

const FAQ_FILE = './data/faqs.json';
const TEST_FILE = './data/testimonials.json';

/* =========================
   HELPERS
========================= */

const load = (file) => {
  if (fs.existsSync(file)) {
    return JSON.parse(fs.readFileSync(file, 'utf-8'));
  }
  return [];
};

const save = (file, data) =>
  fs.writeFileSync(file, JSON.stringify(data, null, 2));

/* =========================
   API - FAQ
========================= */

app.get('/api/faqs', (req, res) => {
  res.json(load(FAQ_FILE));
});

app.post('/api/faqs', (req, res) => {
  const db = load(FAQ_FILE);
  db.push(req.body);
  save(FAQ_FILE, db);
  res.json({ success: true });
});

/* =========================
   API - TESTIMONIALS
========================= */

app.get('/api/testimonials', (req, res) => {
  res.json(load(TEST_FILE));
});

app.post('/api/testimonials', (req, res) => {
  const db = load(TEST_FILE);
  db.push(req.body);
  save(TEST_FILE, db);
  res.json({ success: true });
});

/* =========================
   STATIC FILES
========================= */

app.use(
  '/public',
  express.static(path.join(__dirname, 'public'))
);

/* =========================
   AFFILIATE CTA ENGINE
========================= */

function affiliateCTA() {
  return `
    <div style="margin-top:30px;padding:20px;border-left:4px solid #f59e0b;background:#fff3d6;">
      <h3>🚀 Recommended Tool: JungleScout</h3>
      <p>
        Use JungleScout to find winning Amazon products,
        analyze competition, and scale faster.
      </p>
      <a href="${AFFILIATE_LINK}"
         target="_blank"
         rel="sponsored noopener">
         👉 Try JungleScout
      </a>
    </div>
  `;
}

/* =========================
   FAQ GENERATOR
========================= */

const generateFAQs = () => {

  const categories = [
    "Amazon FBA",
    "Product Research",
    "Jungle Scout",
    "Helium 10",
    "Profit Margins",
    "Supplier Sourcing",
    "SEO Listings",
    "PPC Ads",
    "Scaling Store",
    "Common Mistakes"
  ];

  const faqs = [];

  for (let i = 0; i < 100; i++) {

    const cat = categories[i % categories.length];

    faqs.push({
      id: i + 1,
      question: `What should I know about ${cat}?`,
      answer: `
        Understanding ${cat} is essential for Amazon FBA success.
        Focus on data, testing, and long-term strategy.

        Recommended tool: ${AFFILIATE_LINK}
      `
    });
  }

  save(FAQ_FILE, faqs);
  console.log('✅ 100 FAQs generated');
};

/* =========================
   TESTIMONIAL GENERATOR
========================= */

const generateTestimonials = () => {

  const names = [
    "Alex M.", "Jordan K.", "Taylor R.",
    "Morgan S.", "Casey T.", "Riley D.",
    "Avery L.", "Parker W."
  ];

  const cities = [
    "New York", "London", "Toronto",
    "Berlin", "Sydney", "Dubai",
    "Tokyo", "Paris"
  ];

  const testimonials = [];

  for (let i = 0; i < 100; i++) {

    testimonials.push({
      id: i + 1,
      name: names[i % names.length],
      location: cities[i % cities.length],
      rating: 5,
      text: `
        Used the platform and found it extremely helpful
        for Amazon FBA research and decision making.
        I also used JungleScout:
        ${AFFILIATE_LINK}
      `
    });
  }

  save(TEST_FILE, testimonials);
  console.log('✅ 100 testimonials generated');
};

/* =========================
   INIT DATA
========================= */

generateFAQs();
generateTestimonials();

/* =========================
   FAQ PAGE
========================= */

app.get('/public/faq.html', (req, res) => {

  const html = `
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ System</title>
  </head>

  <body style="font-family:Arial;max-width:900px;margin:auto;padding:20px;">

    <h1>FAQ System</h1>

    ${affiliateCTA()}

    <div id="faq"></div>

    <script>
      fetch('/api/faqs')
        .then(res => res.json())
        .then(data => {

          const container =
            document.getElementById('faq');

          data.forEach(faq => {

            const div =
              document.createElement('div');

            div.innerHTML = \`
              <h3>\${faq.question}</h3>
              <p>\${faq.answer}</p>
              <hr/>
            \`;

            container.appendChild(div);
          });
        });
    </script>

  </body>
  </html>
  `;

  res.send(html);
});

/* =========================
   TESTIMONIAL PAGE
========================= */

app.get('/public/testimonials.html', (req, res) => {

  const html = `
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Testimonials</title>
  </head>

  <body style="font-family:Arial;max-width:900px;margin:auto;padding:20px;">

    <h1>Customer Testimonials</h1>

    ${affiliateCTA()}

    <div id="testimonials"></div>

    <script>
      fetch('/api/testimonials')
        .then(res => res.json())
        .then(data => {

          const container =
            document.getElementById('testimonials');

          data.forEach(t => {

            const div =
              document.createElement('div');

            div.innerHTML = \`
              <strong>\${t.name}</strong>
              (\${t.location})<br/>
              ⭐⭐⭐⭐⭐<br/>
              <p>\${t.text}</p>
              <hr/>
            \`;

            container.appendChild(div);
          });
        });
    </script>

  </body>
  </html>
  `;

  res.send(html);
});

/* =========================
   START SERVER
========================= */

app.listen(3000, () => {
  console.log('🚀 SaaS Engine running on http://localhost:3000');
});
