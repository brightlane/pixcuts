const Twitter = require('twitter');
const axios = require('axios');

/* =========================
   CONFIG (AFFILIATE LOCK)
========================= */

const AFFILIATE_LINK =
  "https://get.junglescout.com/wloofjbvk5mp";

const HASHTAGS =
  "#AmazonFBA #ProductResearch #JungleScout #Ecommerce";

/* =========================
   TWITTER CLIENT
========================= */

const twitterClient = new Twitter({
  consumer_key: 'YOUR_TWITTER_API_KEY',
  consumer_secret: 'YOUR_TWITTER_API_SECRET',
  access_token_key: 'YOUR_TWITTER_ACCESS_TOKEN',
  access_token_secret: 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'
});

/* =========================
   FACEBOOK CONFIG
========================= */

const facebookPageToken =
  'YOUR_FACEBOOK_PAGE_ACCESS_TOKEN';

const facebookPageId =
  'YOUR_FACEBOOK_PAGE_ID';

/* =========================
   TWITTER POST
========================= */

async function postToTwitter(content) {

  try {
    await twitterClient.post(
      'statuses/update',
      { status: content }
    );

    console.log('✅ Posted to Twitter');

  } catch (error) {
    console.error('❌ Twitter error:', error.message);
  }
}

/* =========================
   FACEBOOK POST
========================= */

async function postToFacebook(content) {

  try {
    const url =
      `https://graph.facebook.com/${facebookPageId}/feed`;

    await axios.post(url, null, {
      params: {
        message: content,
        access_token: facebookPageToken
      }
    });

    console.log('✅ Posted to Facebook');

  } catch (error) {
    console.error('❌ Facebook error:', error.message);
  }
}

/* =========================
   SMART POST GENERATOR
========================= */

async function generateSocialMediaPost(blogUrl) {

  if (!blogUrl) {
    throw new Error("Blog URL is required");
  }

  return `
🚀 New Amazon FBA Guide Published!

Discover proven strategies for finding winning products and scaling your store.

📘 Read here:
${blogUrl}

🔥 Recommended Tool:
${AFFILIATE_LINK}

${HASHTAGS}
  `.trim();
}

/* =========================
   MAIN CONTROLLER
========================= */

async function postToSocialMedia(blogUrl) {

  try {

    const content =
      await generateSocialMediaPost(blogUrl);

    // Post everywhere
    await postToTwitter(content);
    await postToFacebook(content);

    console.log("🎯 Social media posting complete");

  } catch (error) {
    console.error(
      "❌ Social media error:",
      error.message
    );
  }
}

/* =========================
   EXAMPLE USAGE
========================= */

const blogUrl =
  'https://brightlane.github.io/Junglescout.com/blog/latest-article';

postToSocialMedia(blogUrl);
