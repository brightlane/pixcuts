#!/usr/bin/env python3
"""
Wondershare PixCut SEO Site Builder
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Domain: brightlane.github.io/pixcuts
200+ keyword pages | 15 blog posts | 13 categories
Purple/violet brand identity
Old-file cleanup baked into workflow

Usage: python3 build.py
Output: ./dist/
"""

import os, json
from datetime import date
from collections import defaultdict

AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949115363004532&atid=pixcutwebs"
SITE_DOMAIN   = "https://brightlane.github.io/pixcuts"
BASE_PATH     = "/pixcuts"
BUILD_DATE    = date.today().isoformat()
DIST          = "dist"
YEAR          = date.today().year

KEYWORDS = []
_seen = set()
def kw(slug, keyword, cat):
    if slug in _seen: return
    _seen.add(slug)
    KEYWORDS.append({"slug": slug, "keyword": keyword, "cat": cat})

# brand
for s,k in [
    ("wondershare-pixcut","Wondershare PixCut"),
    ("pixcut","PixCut background remover"),
    ("pixcut-review","PixCut review 2025"),
    ("pixcut-free","PixCut free background remover"),
    ("pixcut-download","PixCut download"),
    ("pixcut-online","PixCut online tool"),
    ("pixcut-price","PixCut price and plans"),
    ("pixcut-safe","is PixCut safe to use"),
    ("pixcut-legit","is PixCut legit"),
    ("pixcut-worth-it","is PixCut worth it 2025"),
    ("pixcut-features","PixCut features list"),
    ("pixcut-tutorial","PixCut tutorial how to use"),
    ("pixcut-alternative","best PixCut alternative 2025"),
    ("pixcut-vs-remove-bg","PixCut vs Remove.bg comparison"),
    ("pixcut-vs-canva","PixCut vs Canva background remover"),
    ("pixcut-vs-photoshop","PixCut vs Photoshop background remove"),
    ("pixcut-api","PixCut API background removal"),
    ("pixcut-bulk","PixCut bulk background removal"),
    ("pixcut-android-app","PixCut app Android"),
    ("pixcut-iphone-app","PixCut app iPhone iOS"),
    ("wondershare-pixcut-review","Wondershare PixCut review 2025"),
    ("pixcut-coupon","PixCut coupon code 2025"),
    ("pixcut-hd-download","PixCut HD image download free"),
    ("pixcut-free-credits","PixCut free credits how to get"),
]: kw(s,k,"brand")

# background-removal
for s,k in [
    ("ai-background-remover","AI background remover online"),
    ("remove-background-from-image","remove background from image free"),
    ("remove-image-background-online","remove image background online free"),
    ("background-remover-free","background remover free online 2025"),
    ("best-background-remover-2025","best background remover 2025"),
    ("automatic-background-remover","automatic background remover AI"),
    ("background-eraser-online","background eraser online free"),
    ("transparent-background-maker","transparent background maker online"),
    ("remove-white-background","remove white background from image free"),
    ("remove-background-no-download","remove background from image no download"),
    ("one-click-background-removal","one click background removal AI"),
    ("background-removal-no-photoshop","background removal without Photoshop"),
    ("png-transparent-background","make PNG transparent background free"),
    ("jpg-background-remover","JPG background remover online free"),
    ("free-background-removal-tool","free background removal tool 2025"),
    ("remove-background-high-quality","remove background high quality free"),
    ("background-remover-no-watermark","background remover no watermark free"),
    ("ai-photo-background-remove","AI photo background remove tool"),
    ("instant-background-remover","instant background remover online"),
    ("background-remove-transparent-png","remove background transparent PNG download"),
]: kw(s,k,"background-removal")

# bulk-processing
for s,k in [
    ("bulk-background-remover","bulk background remover online"),
    ("batch-background-removal","batch background removal software"),
    ("remove-background-multiple-images","remove background multiple images at once"),
    ("bulk-image-background-remover","bulk image background remover free"),
    ("batch-photo-background-remove","batch photo background remove AI"),
    ("remove-background-20-images","remove background from 20 images"),
    ("bulk-product-photo-background","bulk product photo background remove"),
    ("automated-background-removal","automated background removal ecommerce"),
    ("background-remover-api","background remover API for apps"),
    ("bulk-background-removal-business","bulk background removal for business"),
]: kw(s,k,"bulk-processing")

# ecommerce
for s,k in [
    ("ecommerce-background-remover","ecommerce product background remover"),
    ("product-photo-background-remove","remove background from product photos"),
    ("product-image-white-background","product image white background tool"),
    ("amazon-product-photo-background","Amazon product photo white background"),
    ("shopify-product-image-background","Shopify product image background remover"),
    ("ebay-listing-photo-background","eBay listing photo background remover"),
    ("etsy-product-photo-background","Etsy product photo background remover"),
    ("ecommerce-photo-editing-ai","ecommerce photo editing AI tool"),
    ("product-photography-background","product photography background remover"),
    ("clothing-photo-background-remove","remove background from clothing photos"),
    ("jewelry-photo-background-remove","jewelry photo background remover online"),
    ("furniture-photo-background-remove","furniture product photo background"),
    ("food-photo-background-remove","food photography background remover"),
    ("car-photo-background-remover","car photo background remover online"),
]: kw(s,k,"ecommerce")

# portrait-headshot
for s,k in [
    ("remove-background-from-selfie","remove background from selfie online"),
    ("headshot-background-remover","headshot background remover online free"),
    ("profile-photo-background-remove","profile photo background remover"),
    ("ai-headshot-generator","AI headshot generator online free"),
    ("professional-headshot-ai","professional headshot AI from selfie"),
    ("linkedin-headshot-background","LinkedIn headshot background remover"),
    ("passport-photo-background","passport photo background white online"),
    ("id-photo-background-remover","ID photo background remover online"),
    ("profile-picture-background-change","change profile picture background free"),
    ("person-background-remove-ai","remove person background AI online"),
    ("portrait-background-remover","portrait background remover AI free"),
    ("cv-photo-background-remove","CV resume photo background remover"),
]: kw(s,k,"portrait-headshot")

# design-marketing
for s,k in [
    ("logo-background-remover","logo background remover online free"),
    ("transparent-logo-maker","transparent logo maker online free"),
    ("graphic-design-background-remove","background remover for graphic design"),
    ("social-media-photo-background","social media photo background remover"),
    ("instagram-photo-background-remove","Instagram photo background remover"),
    ("youtube-thumbnail-background","YouTube thumbnail background remover"),
    ("presentation-image-background","remove background for presentation images"),
    ("flyer-design-background-remove","flyer design background remover"),
    ("banner-design-background-remove","banner design background remove tool"),
    ("marketing-photo-background","marketing photo background remover AI"),
    ("t-shirt-design-background","t-shirt design background remover"),
    ("brand-asset-transparent","brand asset transparent PNG maker"),
]: kw(s,k,"design-marketing")

# object-removal
for s,k in [
    ("remove-object-from-photo","remove object from photo online free"),
    ("remove-watermark-from-image","remove watermark from image online"),
    ("photo-object-remover-ai","photo object remover AI online"),
    ("remove-text-from-image","remove text from image online free"),
    ("content-aware-fill-online","content aware fill online free tool"),
    ("unwanted-object-removal","unwanted object removal photo AI"),
    ("scratch-removal-photo","scratch removal from photo online"),
    ("defect-removal-photo-ai","photo defect removal AI tool free"),
    ("remove-blemish-photo-online","remove blemish from photo online"),
    ("photo-cleanup-tool","photo cleanup tool online AI"),
]: kw(s,k,"object-removal")

# image-enhancement
for s,k in [
    ("image-upscaler-online","image upscaler online free"),
    ("upscale-image-no-quality-loss","upscale image without quality loss"),
    ("increase-image-resolution-ai","increase image resolution AI free"),
    ("photo-enhancer-ai","AI photo enhancer online free"),
    ("sharpen-blurry-photo-ai","sharpen blurry photo AI online"),
    ("image-quality-enhancer-free","image quality enhancer free online"),
    ("upscale-image-8x","upscale image to 8x AI free"),
    ("low-resolution-image-fix","fix low resolution image AI online"),
    ("increase-photo-resolution-free","increase photo resolution free"),
    ("ai-image-sharpener","AI image sharpener online free"),
    ("photo-resolution-upscaler","photo resolution upscaler AI"),
    ("enhance-old-photos-ai","enhance old photos AI online"),
]: kw(s,k,"image-enhancement")

# compare
for s,k in [
    ("best-ai-background-remover-2025","best AI background remover 2025"),
    ("remove-bg-alternative-2025","Remove.bg alternative 2025"),
    ("pixcut-vs-removebg","PixCut vs Remove.bg which is better"),
    ("canva-background-remover-alternative","Canva background remover alternative free"),
    ("photoshop-background-alternative","Photoshop background remover alternative free"),
    ("free-vs-paid-background-remover","free vs paid background remover 2025"),
    ("background-remover-comparison","background remover comparison 2025"),
    ("best-bulk-background-remover-2025","best bulk background remover 2025"),
    ("background-remover-no-signup","background remover no signup required"),
    ("remove-bg-free-alternative","Remove.bg free alternative 2025"),
]: kw(s,k,"compare")

# howto
for s,k in [
    ("how-to-remove-background-pixcut","how to remove background with PixCut"),
    ("how-to-remove-white-background","how to remove white background from image"),
    ("how-to-make-transparent-background","how to make transparent background online"),
    ("how-to-bulk-remove-background","how to bulk remove background from images"),
    ("how-to-remove-background-product","how to remove background product photo"),
    ("how-to-change-photo-background","how to change photo background online free"),
    ("how-to-remove-background-logo","how to remove background from logo"),
    ("how-to-remove-person-background","how to remove background behind person"),
    ("how-to-upscale-image-free","how to upscale image online for free"),
    ("how-to-remove-watermark-image","how to remove watermark from image"),
    ("how-to-create-product-photos","how to create professional product photos"),
    ("how-to-remove-background-mobile","how to remove background from photo on mobile"),
    ("how-to-get-transparent-png","how to get transparent PNG from image"),
    ("how-to-make-white-background","how to make white background for product photo"),
]: kw(s,k,"howto")

# platform
for s,k in [
    ("background-remover-windows","background remover for Windows PC"),
    ("background-remover-mac","background remover for Mac"),
    ("background-remover-online-browser","background remover online no install"),
    ("background-remover-android-app","background remover Android app free"),
    ("background-remover-iphone-app","background remover iPhone app free"),
    ("background-remover-no-install","remove background no install needed"),
    ("web-based-background-remover","web based background remover tool"),
    ("background-remover-api-developers","background remover API for developers"),
]: kw(s,k,"platform")

# global
for s,k in [
    ("background-remover-uk","background remover online UK"),
    ("background-remover-india","background remover online India free"),
    ("background-remover-australia","background remover Australia online"),
    ("background-remover-canada","background remover Canada online"),
    ("background-remover-germany","background remover Germany online"),
    ("pixcut-worldwide","PixCut available worldwide"),
    ("ai-background-remover-worldwide","AI background remover worldwide free"),
]: kw(s,k,"global")

# usecase
for s,k in [
    ("photographer-background-remover","background remover for photographers"),
    ("designer-background-remover","background remover for graphic designers"),
    ("youtuber-thumbnail-background","background remover for YouTubers thumbnails"),
    ("real-estate-photo-background","real estate photo background remover"),
    ("fashion-photo-background-remove","fashion photography background remover"),
    ("school-photo-background-remove","school photo background remover"),
    ("freelancer-background-remover","background remover for freelancers"),
    ("small-business-background-remover","background remover for small business"),
    ("blogger-photo-background","background remover for bloggers"),
    ("content-creator-background","background remover for content creators"),
]: kw(s,k,"usecase")

print(f"Keywords loaded: {len(KEYWORDS)}")

COLORS = {
    "brand":              ("#7c3aed","#5b21b6"),
    "background-removal": ("#6366f1","#4338ca"),
    "bulk-processing":    ("#0ea5e9","#0369a1"),
    "ecommerce":          ("#f59e0b","#92400e"),
    "portrait-headshot":  ("#ec4899","#9d174d"),
    "design-marketing":   ("#10b981","#065f46"),
    "object-removal":     ("#ef4444","#991b1b"),
    "image-enhancement":  ("#8b5cf6","#5b21b6"),
    "compare":            ("#475569","#1e293b"),
    "howto":              ("#16a34a","#14532d"),
    "platform":           ("#64748b","#334155"),
    "global":             ("#0284c7","#075985"),
    "usecase":            ("#dc2626","#7f1d1d"),
}
def ac(cat):
    c = COLORS.get(cat, ("#7c3aed","#5b21b6"))
    return c[0], c[1]

CAT_DESC = {
    "brand":              "Everything about Wondershare PixCut &#8212; reviews, pricing, features and tutorials.",
    "background-removal": "Remove backgrounds from any image instantly with AI &#8212; free, online, no Photoshop needed.",
    "bulk-processing":    "Remove backgrounds from up to 20 images at once &#8212; batch processing for ecommerce and business.",
    "ecommerce":          "Professional product photos with clean white backgrounds &#8212; perfect for Amazon, Shopify, Etsy.",
    "portrait-headshot":  "Remove backgrounds from headshots and profile photos &#8212; AI headshot generator included.",
    "design-marketing":   "Remove backgrounds from logos, graphics and marketing images &#8212; clean transparent assets.",
    "object-removal":     "Remove watermarks, objects, text and defects from photos with AI content-aware fill.",
    "image-enhancement":  "Upscale images up to 8x and enhance photo quality with AI &#8212; fix blurry, low-res photos.",
    "compare":            "PixCut vs Remove.bg, Canva, Adobe &#8212; find the best AI background remover 2025.",
    "howto":              "Step-by-step guides for every PixCut feature and use case.",
    "platform":           "PixCut works on any browser &#8212; Windows, Mac, Android and iPhone. No installation needed.",
    "global":             "Wondershare PixCut available worldwide in any browser.",
    "usecase":            "PixCut for photographers, designers, ecommerce sellers, YouTubers and businesses.",
}


CSS = """<style>
:root{--ink:#0f172a;--paper:#faf5ff;--card:#fff;--border:#ede9fe;--muted:#64748b;
  --dark:#0f172a;--ha:#7c3aed;--hb:#5b21b6;--fa:rgba(124,58,237,.08)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:'Segoe UI',system-ui,-apple-system,sans-serif;font-size:16px;line-height:1.65;overflow-x:hidden}
a{color:var(--ha);text-decoration:none}a:hover{text-decoration:underline}
nav{position:sticky;top:0;z-index:100;background:var(--dark);display:flex;align-items:center;justify-content:space-between;padding:0 clamp(1rem,4vw,2.5rem);height:58px;box-shadow:0 1px 0 rgba(255,255,255,.07)}
.nl{font-size:1.2rem;color:#fff;font-weight:800;letter-spacing:-.03em;white-space:nowrap}.nl span{color:#a78bfa}
.nlinks{display:flex;gap:1.4rem;align-items:center}
.nlinks a{color:rgba(255,255,255,.6);font-size:.82rem;font-weight:500;white-space:nowrap}
.nlinks a:hover{color:#fff;text-decoration:none}
.ncta{background:var(--ha)!important;color:#fff!important;padding:.38rem 1.05rem;border-radius:6px;font-weight:700!important;font-size:.82rem!important}
.hero{background:linear-gradient(135deg,#1e1b4b 0%,#4c1d95 40%,#7c3aed 75%,#a78bfa 100%);color:#fff;padding:clamp(3.5rem,8vw,6.5rem) clamp(1rem,5vw,3rem);text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 50% at 50% 110%,rgba(167,139,250,.4) 0%,transparent 70%);pointer-events:none}
.eyebrow{display:inline-block;border-radius:100px;font-size:.7rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;padding:.26rem .95rem;margin-bottom:1.25rem;border:1px solid rgba(167,139,250,.5);color:#c4b5fd;background:rgba(167,139,250,.1)}
h1{font-size:clamp(2rem,5.5vw,3.9rem);line-height:1.05;letter-spacing:-.035em;max-width:880px;margin:0 auto 1.1rem;font-weight:800}
h1 em{color:#ddd6fe;font-style:italic}
.hsub{font-size:clamp(.95rem,2vw,1.12rem);color:rgba(255,255,255,.78);max-width:620px;margin:0 auto 2.3rem}
.btn-p{background:var(--ha);color:#fff;padding:.88rem 2.1rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(124,58,237,.5);text-decoration:none}
.btn-s{background:transparent;border:1px solid rgba(255,255,255,.3);color:rgba(255,255,255,.85);padding:.88rem 2.1rem;border-radius:8px;font-weight:600;font-size:1rem;display:inline-block}
.btn-s:hover{background:rgba(255,255,255,.1);text-decoration:none}
.btn-w{background:#fff;color:var(--ha);padding:.88rem 2.3rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-w:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.18);text-decoration:none}
.btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.stats{display:flex;justify-content:center;gap:clamp(1.5rem,4vw,3.5rem);margin-top:3.5rem;padding-top:3rem;border-top:1px solid rgba(255,255,255,.15);flex-wrap:wrap}
.stat-n{font-size:clamp(1.8rem,3.5vw,2.6rem);color:#fff;display:block;font-weight:800;line-height:1}
.stat-l{font-size:.7rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.07em;margin-top:.3rem}
section{padding:clamp(3rem,7vw,5.5rem) clamp(1rem,5vw,2.5rem)}
.container{max-width:1100px;margin:0 auto}
.sec-ey{font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ha);margin-bottom:.55rem}
h2{font-size:clamp(1.7rem,3.5vw,2.55rem);line-height:1.1;letter-spacing:-.025em;margin-bottom:.75rem;font-weight:800}
h3{font-size:1.03rem;font-weight:700;margin-bottom:.42rem}
.sec-sub{color:var(--muted);max-width:590px;font-size:1rem;margin-bottom:3rem;line-height:1.7}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.4rem}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem;transition:box-shadow .2s,transform .2s}
.card:hover{box-shadow:0 10px 36px rgba(124,58,237,.1);transform:translateY(-3px)}
.fi{width:46px;height:46px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:1.1rem;background:var(--fa)}
.card p,.card li{font-size:.87rem;color:var(--muted);line-height:1.7}
.card ul{padding-left:1.2rem;margin-top:.42rem}.card ul li{margin-bottom:.28rem}
.prose{max-width:780px;color:var(--muted);font-size:.95rem;line-height:1.82}
.prose p{margin-bottom:1.1rem}
.prose h2,.prose h3{color:var(--ink);margin:1.9rem 0 .5rem;font-weight:700}
.prose ul,.prose ol{padding-left:1.4rem;margin-bottom:1.1rem}
.prose li{margin-bottom:.4rem}
.prose strong{color:var(--ink);font-weight:600}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2rem;margin-top:2.5rem}
.step{text-align:center}
.sn{display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;border-radius:50%;background:var(--ha);color:#fff;font-size:1.25rem;font-weight:800;margin-bottom:.9rem}
.step h3{font-size:.94rem;margin-bottom:.3rem}
.step p{font-size:.82rem;color:var(--muted);line-height:1.6}
.tbl-wrap{overflow-x:auto;margin-top:2rem}
table{width:100%;border-collapse:collapse;font-size:.85rem;min-width:600px}
th{padding:.88rem 1rem;text-align:left;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;border-bottom:2px solid var(--border)}
td{padding:.88rem 1rem;border-bottom:1px solid var(--border)}
tr:hover td{background:#faf5ff}
.hl{color:var(--ha);font-weight:700}.ck{color:#16a34a;font-weight:600}.cr{color:#d1d5db}.cp{color:#f59e0b}
.faq-list{max-width:820px}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:.7rem;overflow:hidden}
.faq-q{padding:1.05rem 1.35rem;font-weight:700;font-size:.93rem;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
.faq-q::after{content:'+';font-size:1.3rem;color:var(--ha);flex-shrink:0;line-height:1}
.faq-item.open .faq-q::after{content:'\2212'}
.faq-a{padding:0 1.35rem 1.05rem;font-size:.87rem;color:var(--muted);line-height:1.75;display:none}
.faq-item.open .faq-a{display:block}
.cta-strip{background:linear-gradient(135deg,var(--hb) 0%,var(--ha) 100%);color:#fff;text-align:center;padding:clamp(3.5rem,7vw,6.5rem) clamp(1rem,5vw,3rem)}
.cta-strip h2{color:#fff;margin-bottom:.88rem}
.cta-strip p{color:rgba(255,255,255,.82);max-width:520px;margin:0 auto 2.3rem;font-size:1rem}
.bcrumb{font-size:.77rem;color:var(--muted);padding:.88rem clamp(1rem,5vw,2.5rem);max-width:1100px;margin:0 auto}
.bcrumb a{color:var(--muted)}.bcrumb a:hover{color:var(--ha);text-decoration:none}
.kw-cloud{display:flex;flex-wrap:wrap;gap:.46rem;margin-top:1.5rem}
.kw{background:var(--card);border:1px solid var(--border);border-radius:6px;padding:.27rem .72rem;font-size:.77rem;color:var(--muted)}
a.kw:hover{border-color:var(--ha);color:var(--ha);text-decoration:none}
.tcard{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem}
.stars{color:#fbbf24;font-size:.95rem;margin-bottom:.88rem}
.ttext{font-size:.88rem;color:var(--ink);margin-bottom:1.3rem;line-height:1.78;font-style:italic}
.tauthor{font-weight:700;font-size:.8rem;color:var(--muted)}
.dark-sec{background:var(--dark);color:#fff}
.dark-sec .sec-ey{color:#a78bfa}.dark-sec h2{color:#fff}
.dark-sec .kw{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.14);color:rgba(255,255,255,.7)}
.notice{background:rgba(124,58,237,.08);border:1px solid rgba(124,58,237,.25);border-radius:8px;padding:.92rem 1.35rem;font-size:.83rem;color:var(--muted);margin-top:2rem}
.badge{display:inline-block;font-size:.67rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;padding:.19rem .56rem;border-radius:4px;background:rgba(124,58,237,.1);color:var(--ha)}
.uc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:1rem;margin-top:2rem}
.uc-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.2rem;text-align:center;transition:box-shadow .2s,transform .2s;display:block}
.uc-card:hover{box-shadow:0 8px 24px rgba(124,58,237,.12);transform:translateY(-2px);text-decoration:none}
.uc-icon{font-size:1.8rem;display:block;margin-bottom:.55rem}
.uc-label{font-size:.83rem;font-weight:700;color:var(--ink);display:block}
.uc-sub{font-size:.73rem;color:var(--muted);margin-top:.2rem;display:block}
footer{background:#0c0a1e;color:rgba(255,255,255,.48);padding:clamp(2.5rem,5vw,4rem) clamp(1rem,5vw,2.5rem) 2rem}
.fg{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:2.5rem;margin-bottom:2.5rem}
.fn{font-size:1.3rem;color:#fff;font-weight:800;letter-spacing:-.03em;margin-bottom:.6rem}
.fn span{color:#a78bfa}
.fdesc{font-size:.79rem;color:rgba(255,255,255,.4);max-width:230px;margin-bottom:.9rem;line-height:1.6}
.fc h4{color:#fff;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.82rem}
.fc ul{list-style:none}.fc ul li{margin-bottom:.38rem}
.fc ul li a{color:rgba(255,255,255,.44);font-size:.79rem}
.fc ul li a:hover{color:#fff;text-decoration:none}
.fb{max-width:1100px;margin:0 auto;border-top:1px solid rgba(255,255,255,.08);padding-top:1.75rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.75rem;font-size:.72rem}
.aff{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:6px;padding:.44rem .98rem;font-size:.72rem;margin-top:.75rem;max-width:530px;line-height:1.5}
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.fg{grid-template-columns:1fr}.nlinks a:not(.ncta){display:none}h1{font-size:2rem}.steps{grid-template-columns:1fr 1fr}}
@media(max-width:400px){.steps{grid-template-columns:1fr}}
</style>"""

FAQ_JS = """<script>
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>{
    const item=q.parentElement;
    document.querySelectorAll('.faq-item.open').forEach(o=>{if(o!==item)o.classList.remove('open')});
    item.classList.toggle('open');
  });
});
</script>"""

def NAV():
    return (f'<nav><a class="nl" href="{BASE_PATH}/">Pix<span>Cut</span></a>'
            f'<div class="nlinks">'
            f'<a href="{BASE_PATH}/">Home</a>'
            f'<a href="{BASE_PATH}/features.html">Features</a>'
            f'<a href="{BASE_PATH}/how-it-works.html">How It Works</a>'
            f'<a href="{BASE_PATH}/compare.html">Compare</a>'
            f'<a href="{BASE_PATH}/faq.html">FAQ</a>'
            f'<a href="{BASE_PATH}/blog.html">Blog</a>'
            f'<a href="{AFFILIATE_URL}" class="ncta" target="_blank" rel="nofollow sponsored">&#8659; Try Free</a>'
            f'</div></nav>')

def FOOTER():
    return (f'<footer><div class="fg"><div>'
            f'<div class="fn">Pix<span>Cut</span></div>'
            f'<p class="fdesc">Wondershare PixCut &#8212; AI background remover. Remove, replace, bulk process, upscale and enhance images. Free to start, no install.</p>'
            f'<div class="aff">&#128279; Affiliate disclosure: Links on this site are affiliate links. We earn a commission at no extra cost to you.</div>'
            f'</div>'
            f'<div class="fc"><h4>Features</h4><ul>'
            f'<li><a href="{BASE_PATH}/remove-background-from-image.html">Background Removal</a></li>'
            f'<li><a href="{BASE_PATH}/bulk-background-remover.html">Bulk Removal</a></li>'
            f'<li><a href="{BASE_PATH}/remove-object-from-photo.html">Object Remover</a></li>'
            f'<li><a href="{BASE_PATH}/image-upscaler-online.html">Image Upscaler</a></li>'
            f'<li><a href="{BASE_PATH}/ai-headshot-generator.html">AI Headshots</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Use Cases</h4><ul>'
            f'<li><a href="{BASE_PATH}/ecommerce-background-remover.html">Ecommerce</a></li>'
            f'<li><a href="{BASE_PATH}/logo-background-remover.html">Logos</a></li>'
            f'<li><a href="{BASE_PATH}/headshot-background-remover.html">Headshots</a></li>'
            f'<li><a href="{BASE_PATH}/product-photo-background-remove.html">Products</a></li>'
            f'<li><a href="{BASE_PATH}/remove-watermark-from-image.html">Watermarks</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Resources</h4><ul>'
            f'<li><a href="{BASE_PATH}/faq.html">FAQ</a></li>'
            f'<li><a href="{BASE_PATH}/blog.html">Blog</a></li>'
            f'<li><a href="{BASE_PATH}/compare.html">Comparisons</a></li>'
            f'<li><a href="{BASE_PATH}/glossary.html">Glossary</a></li>'
            f'<li><a href="{BASE_PATH}/keywords.html">All Topics</a></li>'
            f'<li><a href="{BASE_PATH}/sitemap.xml">Sitemap</a></li>'
            f'</ul></div></div>'
            f'<div class="fb">'
            f'<span>&#169; {YEAR} PixCut Guide. PixCut is a product of Wondershare Technology Co., Ltd.</span>'
            f'<span>Web &#183; Windows &#183; Mac &#183; Android &#183; iOS</span>'
            f'</div></footer>')

def BC(items):
    parts=[]
    for label,url in items:
        if url: parts.append(f'<a href="{url}">{label}</a>')
        else: parts.append(label)
    return '<div class="bcrumb container">' + ' &rsaquo; '.join(parts) + '</div>'

def CTA(h="Remove Image Backgrounds Instantly &#8212; Try PixCut Free",
        p="AI background removal, bulk processing up to 20 images, object eraser, 8x upscaler and AI headshots. Free to start."):
    return (f'<div class="cta-strip"><h2>{h}</h2><p>{p}</p>'
            f'<a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a></div>')

def SW_SCHEMA():
    d={"@context":"https://schema.org","@type":"SoftwareApplication",
       "name":"Wondershare PixCut","operatingSystem":"Web, Windows, macOS, Android, iOS",
       "applicationCategory":"MultimediaApplication",
       "offers":{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free tier available"},
       "description":"PixCut is an AI-powered online background remover. Removes backgrounds, objects and watermarks from images instantly. Bulk processing up to 20 images, 8x upscaler, AI headshot generator.",
       "url":AFFILIATE_URL,
       "publisher":{"@type":"Organization","name":"Wondershare Technology"},
       "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.7","reviewCount":"8241","bestRating":"5"}}
    return '<script type="application/ld+json">'+json.dumps(d)+'</script>'

def BC_SCHEMA(items):
    els=[{"@type":"ListItem","position":i+1,"name":l,"item":SITE_DOMAIN+"/"+u if u else SITE_DOMAIN} for i,(l,u) in enumerate(items)]
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":els})+'</script>'

def FAQ_SCHEMA(pairs):
    items=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":items})+'</script>'

def ART_SCHEMA(title,desc,pub):
    d={"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
       "datePublished":pub,"dateModified":BUILD_DATE,
       "author":{"@type":"Organization","name":"PixCut Guide"},
       "publisher":{"@type":"Organization","name":"PixCut Guide"}}
    return '<script type="application/ld+json">'+json.dumps(d)+'</script>'

def HEAD(title,desc,canon,extra="",og_type="website"):
    return ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            "<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            f"<title>{title}</title>\n"
            f"<meta name=\"description\" content=\"{desc}\"/>\n"
            f"<link rel=\"canonical\" href=\"{SITE_DOMAIN}/{canon}\"/>\n"
            f"<meta property=\"og:title\" content=\"{title}\"/>\n"
            f"<meta property=\"og:description\" content=\"{desc}\"/>\n"
            f"<meta property=\"og:type\" content=\"{og_type}\"/>\n"
            f"<meta property=\"og:url\" content=\"{SITE_DOMAIN}/{canon}\"/>\n"
            "<meta property=\"og:site_name\" content=\"PixCut Guide\"/>\n"
            "<meta name=\"twitter:card\" content=\"summary_large_image\"/>\n"
            f"<meta name=\"twitter:title\" content=\"{title}\"/>\n"
            f"<meta name=\"twitter:description\" content=\"{desc}\"/>\n"
            "<meta name=\"robots\" content=\"index,follow\"/>\n"
            +CSS+"\n"+SW_SCHEMA()+"\n"+extra+"\n</head>")


FEATURES=[
    ("&#9986;","AI Background Remover","Upload any image and AI instantly removes the background &#8212; accurate edges, transparent PNG output, free to start.",
     ["Any image type: people, products, logos","Transparent PNG output","Sharp edge detection including hair","Free to start"]),
    ("&#128230;","Bulk Removal &#8212; Up to 20","Remove backgrounds from up to 20 images simultaneously &#8212; batch process entire product catalogues in minutes.",
     ["Up to 20 images at once","Same AI quality as single images","Great for ecommerce catalogues","Save hours of manual editing"]),
    ("&#128247;","Object &amp; Watermark Remover","Remove watermarks, objects, text, scratches and defects from photos using AI content-aware fill.",
     ["Remove watermarks","Erase unwanted objects and text","Fix scratches and defects","AI content-aware fill"]),
    ("&#128200;","Image Upscaler &#8212; Up to 8x","Upscale images up to 8x without quality loss &#8212; fix blurry and low-resolution photos with AI enhancement.",
     ["Upscale up to 8x original size","No visible quality loss","Fix blurry photos","AI sharpening and detail"]),
    ("&#128736;","Background Replacer","Replace removed backgrounds with solid colours, custom images or patterns from PixCut's library.",
     ["Solid colour backgrounds","Upload your own background","Background library included","Preview before download"]),
    ("&#129312;","AI Headshot Generator","Transform selfies into professional AI headshots &#8212; perfect for LinkedIn, CVs and profile photos.",
     ["Professional headshot styles","From selfie to LinkedIn photo","Multiple style options","No photographer needed"]),
    ("&#127760;","API for Developers","Integrate PixCut's AI background removal into your own apps with a simple REST API.",
     ["REST API integration","High volume processing","Developer documentation","Commercial usage supported"]),
    ("&#128241;","Web, iOS &amp; Android","Works in any browser on any device &#8212; no installation, no download, always up to date.",
     ["No install needed","Any browser on any device","iOS and Android apps","Free to start"]),
]

def FEATURES_GRID():
    cards=""
    for icon,name,desc,buls in FEATURES:
        li="".join(f"<li>{b}</li>" for b in buls)
        cards+=f'<div class="card"><div class="fi">{icon}</div><h3>{name}</h3><p>{desc}</p><ul>{li}</ul></div>'
    return f'<div class="grid2">{cards}</div>'

TESTIMONIALS=[
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I run an Etsy jewellery shop with 300+ products. Removing backgrounds used to take me hours in Photoshop every week. PixCut batch removes 20 product photos in under 2 minutes. The accuracy on thin chain links and gemstones is incredible.","Sarah K.","London, UK &#127468;&#127463;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","As a real estate photographer I need clean property images fast. PixCut removes distracting backgrounds from listing photos in seconds. The object removal also handles minor issues I'd otherwise spend time fixing in Lightroom.","James T.","Chicago, USA &#127482;&#127480;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I used PixCut's AI Headshot Generator from a regular selfie and now use it as my LinkedIn photo. Saved me $250 on a professional headshot session. Multiple colleagues asked which studio I used.","Priya M.","Mumbai, India &#127470;&#127475;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","Ich verkaufe Mode auf Amazon. Jedes Produktfoto braucht wei&#223;en Hintergrund. PixCut macht das in Sekunden &#8212; perfekte Kanten auch bei d&#252;nner Spitze und Mesh. Spart mir jeden Tag Stunden.","Klaus B.","Berlin, Deutschland &#127465;&#127466;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","The image upscaler is remarkable. I had old low-resolution product photos from years ago &#8212; PixCut upscaled them to usable quality. Saved me a complete reshooting session worth thousands of dollars.","Tom H.","Sydney, Australia &#127462;&#127482;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","J'utilise PixCut pour tous mes visuels Instagram. La suppression de fond est parfaite et le r&#233;sultat est professionnel. Beaucoup plus rapide et moins cher que Photoshop pour ce que j'ai besoin.","Marie D.","Paris, France &#127467;&#127479;"),
]

def TESTIMONIALS_GRID():
    cards="".join(f'<div class="tcard"><div class="stars">{s}</div><p class="ttext">"{t}"</p><div class="tauthor">{n} &#8212; {l}</div></div>' for s,t,n,l in TESTIMONIALS)
    return f'<div class="grid3">{cards}</div>'

FAQ_GLOBAL=[
    ("What is Wondershare PixCut?","Wondershare PixCut is an AI-powered online background remover that automatically removes backgrounds from any image in seconds. It also removes objects and watermarks, upscales images up to 8x, generates AI headshots and replaces backgrounds."),
    ("Is PixCut free to use?","Yes &#8212; PixCut has a free tier for background removal with standard resolution downloads. HD downloads and bulk processing of more than a few images require a paid plan."),
    ("How does PixCut remove backgrounds?","PixCut uses AI trained on millions of images to identify the foreground subject and separate it from the background automatically. Upload any image &#8212; the AI does everything in seconds with no manual selection or Photoshop skills required."),
    ("Does PixCut handle hair and fine details?","Yes &#8212; PixCut's AI specifically handles complex edges including hair, fur, transparent objects and fine details. The AI preserves natural edge textures rather than creating hard cutout edges."),
    ("Can I remove backgrounds from multiple images at once?","Yes &#8212; PixCut's bulk processing removes backgrounds from up to 20 images simultaneously. All 20 results are ready within a minute or two."),
    ("Does PixCut need to be installed?","No &#8212; PixCut is primarily web-based and works in any browser on any device. No installation, no download. iOS and Android apps are also available."),
    ("Can I replace the background after removing it?","Yes &#8212; PixCut lets you replace the removed background with a solid colour, upload a custom background, or choose from PixCut's background library."),
    ("Does PixCut have an image upscaler?","Yes &#8212; PixCut upscales images up to 8x the original dimensions using AI, adding genuine detail rather than just enlarging pixels. Fix blurry and low-resolution images."),
    ("What is the AI Headshot Generator?","PixCut's AI Headshot Generator transforms a regular selfie into a professional headshot-style portrait suitable for LinkedIn, CVs and professional profiles. Multiple styles available."),
    ("Is PixCut better than Remove.bg?","PixCut matches Remove.bg's background removal quality and adds features Remove.bg lacks: object and watermark removal, image upscaler up to 8x, AI headshot generator, and a more generous free tier."),
]

def FAQ_BLOCK(pairs):
    items="".join(f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q,a in pairs)
    return f'<div class="faq-list">{items}</div>'

def related_cloud(kw_data,n=24):
    same=[k for k in KEYWORDS if k["cat"]==kw_data["cat"] and k["slug"]!=kw_data["slug"]]
    diff=[k for k in KEYWORDS if k["cat"]!=kw_data["cat"]]
    pool=(same+diff)[:n]
    links="".join(f'<a class="kw" href="{BASE_PATH}/{r["slug"]}.html">{r["keyword"]}</a>' for r in pool)
    return f'<div class="kw-cloud">{links}</div>'

def cat_deep(cat,keyword):
    bodies={
"background-removal":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">How It Works</div><h2>AI Background Removal &#8212; How PixCut Does It</h2>'
    '<div class="prose">'
    '<p>Traditional background removal requires either manual masking in Photoshop &#8212; a skill that takes years to develop and 5-15 minutes per image even when mastered &#8212; or simple colour-based selection tools that fail on anything more complex than a plain studio shot. PixCut\'s AI is trained on hundreds of millions of images and understands what the foreground subject is regardless of background complexity.</p>'
    '<h3>The AI Process</h3>'
    '<p>When you upload an image, PixCut\'s AI analyses the entire image simultaneously. It identifies what the primary subject is &#8212; person, product, animal, object &#8212; traces the boundary including complex areas like hair and fine detail, and separates foreground from background in a single pass. The result is a transparent PNG that preserves natural edge textures. No hard artificial cutout lines.</p>'
    '<h3>What PixCut Handles</h3>'
    '<p>The most challenging background removal subjects &#8212; loose curly hair, fine jewellery chains, transparent product packaging, fabrics with open weave &#8212; are where older tools fail. PixCut\'s model is specifically trained on these difficult categories. A person with loose curly hair against a complex background is processed as accurately as a simple product on a white surface.</p>'
    '<h3>Manual Refinement Available</h3>'
    '<p>After AI removal, use the Erase brush to remove any remaining background areas the AI kept, or the Restore brush to recover any subject area accidentally removed. This gives you both the speed of AI and the precision of manual work when needed.</p>'
    '</div></div></section>'),

"ecommerce":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Ecommerce Guide</div><h2>Product Photos with White Backgrounds &#8212; Automated</h2>'
    '<div class="prose">'
    '<p>Amazon requires main product images on a pure white background (RGB 255,255,255) with the product filling at least 85% of the frame. Similar requirements apply to Walmart Marketplace, eBay and most major ecommerce platforms. Meeting this across hundreds of product SKUs used to mean a professional photography studio or hours of Photoshop work per photo. PixCut automates this entirely.</p>'
    '<h3>Bulk Processing for Catalogues</h3>'
    '<p>PixCut removes backgrounds from up to 20 images simultaneously. For a seller with 500 products, this transforms what was a multi-week editing task into an afternoon. Upload a batch of product photos, select white as the replacement background, download the processed batch. Every photo meets marketplace requirements.</p>'
    '<h3>Difficult Product Categories</h3>'
    '<p>Jewellery with thin chains, transparent glass products, clothing with fine mesh, lace or sheer fabric, products with reflective surfaces &#8212; all categories where background removal is notoriously difficult. PixCut handles each with specific AI training, preserving the natural appearance of complex materials.</p>'
    '<h3>Lifestyle Images from One Photo</h3>'
    '<p>Remove the original background, then use PixCut\'s Background Replacer to add environment scenes &#8212; product in a kitchen, bedroom, outdoor setting. This creates multiple lifestyle images for social media from a single original product photo, without a second photoshoot.</p>'
    '</div></div></section>'),

"portrait-headshot":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Portrait Guide</div><h2>Remove Portrait Backgrounds &amp; Generate AI Headshots</h2>'
    '<div class="prose">'
    '<p>Portrait background removal requires the highest accuracy of all image types. Hair &#8212; especially loose, curly or fine hair &#8212; is the hardest subject for background removal AI. PixCut\'s model was specifically trained on portrait images to handle the full range of hair types, skin tones and portrait compositions.</p>'
    '<h3>Profile Photos and LinkedIn</h3>'
    '<p>LinkedIn and company websites require neutral or white background profile photos. With PixCut, remove the background from any existing casual photo and replace it with white or a professional neutral colour. The result is indistinguishable from a properly studio-shot profile photo &#8212; without the studio cost.</p>'
    '<h3>Passport and ID Photos</h3>'
    '<p>Most countries require passport photos on a specific background colour (white, off-white or light grey). PixCut removes the original background and applies the exact required colour. The photo still needs correct lighting and composition, but the background requirement is handled instantly.</p>'
    '<h3>AI Headshot Generator &#8212; Selfie to Professional</h3>'
    '<p>PixCut\'s AI Headshot Generator goes further than background removal: it transforms casual selfies into professional headshot-style portraits using AI. Multiple professional styles (formal business, creative, academic) are applied to produce headshots suitable for LinkedIn, CVs and professional profiles. The AI adjusts lighting, colour grading and framing &#8212; producing results colleagues and clients cannot distinguish from a professional studio session.</p>'
    '</div></div></section>'),

"bulk-processing":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Bulk Processing Guide</div><h2>Remove Backgrounds from Multiple Images Simultaneously</h2>'
    '<div class="prose">'
    '<p>Manual background removal takes 5-15 minutes per image in Photoshop for a skilled editor. For a product catalogue of 300 items, that\'s 25-75 hours of editing work. PixCut\'s batch mode handles 20 images at a time, each completing in seconds. A 300-image catalogue takes an afternoon instead of two weeks.</p>'
    '<h3>How Batch Mode Works</h3>'
    '<p>Upload up to 20 images in a single session. PixCut\'s AI processes each image in parallel. All 20 results are available within 1-2 minutes. Download individually or as a ZIP. Repeat with the next set. For 200 product images, this means 10 batches of 20 &#8212; completing in under 30 minutes total.</p>'
    '<h3>Consistency Across the Catalogue</h3>'
    '<p>Manual background removal across a large catalogue produces inconsistent results &#8212; different edge treatment, different colour accuracy, different levels of transparency. PixCut\'s AI applies the same algorithm to every image, producing consistent edge quality and output specification throughout the entire catalogue.</p>'
    '<h3>API for Larger Volumes</h3>'
    '<p>For volumes beyond 20 images at a time, PixCut\'s REST API allows programmatic background removal at any scale. Integrate into your product management workflow, trigger removal automatically on new photo uploads, and receive transparent PNG outputs directly into your storage system.</p>'
    '</div></div></section>'),

"object-removal":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Object Removal Guide</div><h2>Remove Watermarks, Objects &amp; Defects from Photos</h2>'
    '<div class="prose">'
    '<p>PixCut\'s content-aware fill removes specific objects, areas or defects from within photos. The AI analyses surrounding pixels and fills the removed area with plausible matching content &#8212; making the removal invisible rather than leaving an obvious blank patch.</p>'
    '<h3>Watermark Removal</h3>'
    '<p>Watermarks covering part of a product image or document can be removed using the object remover. Paint over the watermark with the brush tool. PixCut\'s AI fills the area with content matching the surrounding pixels. The removal leaves no visible trace of the original watermark.</p>'
    '<h3>Unwanted Object Removal</h3>'
    '<p>Photobombing subjects, distracting background elements, cables, price tags, stickers &#8212; any unwanted element within an otherwise good photo can be removed. The brush size adjusts for different object sizes. Content-aware fill produces realistic results even in textured backgrounds.</p>'
    '<h3>Photo Defect Repair</h3>'
    '<p>Scratches, dust spots and sensor artifacts from scanned photos or camera contamination are repaired with the same tool. Particularly useful for restoring old scanned photographs where dust and scratches reduce visual quality.</p>'
    '</div></div></section>'),

"image-enhancement":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Enhancement Guide</div><h2>Upscale Images to 8x &#8212; AI Enhancement</h2>'
    '<div class="prose">'
    '<p>Traditional image upscaling simply enlarges pixels &#8212; producing blurry, pixelated results. AI upscaling adds plausible detail using deep learning trained on millions of high-quality images. The result genuinely looks sharper at larger sizes, not just stretched.</p>'
    '<h3>Upscale to 8x</h3>'
    '<p>PixCut upscales images up to 8x the original dimensions. A 200x200 pixel product thumbnail becomes 1600x1600 with AI detail. An old 2MP phone photo becomes a usable 16MP equivalent. Small images that couldn\'t previously be printed large or displayed on high-resolution screens become viable.</p>'
    '<h3>Who Uses Image Upscaling</h3>'
    '<p><strong>Ecommerce sellers:</strong> Old product photos taken when cameras had lower resolution can be upscaled to current standards without reshooting. <strong>Photographers:</strong> Old digital scans or cropped photos can be brought back to full usable resolution. <strong>Marketers:</strong> Low-resolution social media images downloaded from platforms can be enhanced for use in print or large digital contexts. <strong>Archivists:</strong> Historic photographs scanned at limited resolution can be enhanced for display and preservation.</p>'
    '<h3>Photo Enhancer</h3>'
    '<p>Beyond upscaling, PixCut\'s photo enhancer automatically corrects blurry, hazy or poorly exposed images. AI-adaptive corrections including sharpening, white balance, colour enhancement and exposure compensation improve image quality without requiring manual adjustment skills.</p>'
    '</div></div></section>'),

"design-marketing":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Design Guide</div><h2>Background Removal for Designers &amp; Marketers</h2>'
    '<div class="prose">'
    '<p>For graphic designers and marketing teams, background removal is one of the most frequent and repetitive production tasks &#8212; isolating subjects for composites, creating transparent assets for templates, preparing images for brand guidelines. PixCut automates this bottleneck, freeing designer time for the creative work that requires human judgment.</p>'
    '<h3>Logo and Brand Asset Preparation</h3>'
    '<p>Logos are frequently needed as transparent PNG files but are often only available on white or coloured backgrounds. PixCut removes the background from any logo in seconds, producing a clean transparent PNG with accurate edge detail ready for placement on any colour or background in any design tool.</p>'
    '<h3>Social Media Content at Scale</h3>'
    '<p>Instagram, LinkedIn and TikTok content templates require isolated subject images &#8212; people, products, objects &#8212; on branded backgrounds. PixCut removes backgrounds automatically, providing the transparent PNG that Canva, Adobe Express, Figma or any other tool places over templates. For agencies managing social content at scale, PixCut\'s bulk processing handles entire content batches.</p>'
    '<h3>Print and Digital Marketing</h3>'
    '<p>Flyers, banners, email headers, presentations &#8212; all require isolated images. PixCut\'s batch capability means a full marketing campaign\'s worth of isolated subjects can be processed in minutes rather than individual Photoshop sessions for each asset.</p>'
    '</div></div></section>'),

"compare":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Honest Comparison</div><h2>'+keyword+' &#8212; Detailed Analysis</h2>'
    '<div class="prose">'
    '<p>Choosing the right background removal tool depends on your volume, use case and budget. Here is an honest comparison.</p>'
    '<h3>vs Remove.bg</h3>'
    '<p>Remove.bg is the best-known background remover with strong AI accuracy. PixCut matches its core background removal quality and adds features Remove.bg lacks entirely: object and watermark removal, image upscaler up to 8x, AI headshot generator, and background replacer. PixCut\'s free tier is also more generous with downloads. For users who need more than background removal alone, PixCut is the more complete solution.</p>'
    '<h3>vs Canva Background Remover</h3>'
    '<p>Canva Pro\'s background remover requires a subscription ($13+/month) and only works within Canva\'s design editor. PixCut works standalone, handles complex subjects &#8212; especially hair &#8212; with better accuracy than Canva\'s tool, and doesn\'t require a design subscription to access background removal.</p>'
    '<h3>vs Photoshop</h3>'
    '<p>Photoshop produces excellent background removal but costs $21+/month, requires installation and hardware, and takes significant time to learn. PixCut produces comparable results in any browser in under 10 seconds, free of charge, with zero learning curve. For background removal specifically, PixCut is faster and more accessible than Photoshop for the vast majority of use cases.</p>'
    '</div></div></section>'),
    }
    body=bodies.get(cat)
    if body: return body
    return (f'<section style="background:#fff"><div class="container">'
            f'<div class="sec-ey">Complete Guide</div>'
            f'<h2>{keyword} &#8212; Overview</h2>'
            f'<div class="prose">'
            f'<p>Wondershare PixCut is the leading solution for {keyword.lower()}. '
            f'AI background removal works on any image in seconds &#8212; no Photoshop, no installation, free to start. '
            f'Bulk removal for up to 20 images, object remover, 8x upscaler and AI headshots included.</p>'
            f'<p>Whether you\'re an ecommerce seller needing white product backgrounds, a designer needing transparent logo PNGs, '
            f'or a professional needing a LinkedIn headshot, PixCut handles every scenario in one browser-based tool.</p>'
            f'</div>'
            f'<div style="margin-top:2rem">'
            f'<a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
            f'</div></div></section>')

def build_keyword_page(kw_data):
    slug=kw_data["slug"]; keyword=kw_data["keyword"]; cat=kw_data["cat"]
    a1,a2=ac(cat)
    title  = f"{keyword} &#8212; Wondershare PixCut | {YEAR}"
    desc   = f"Looking for {keyword.lower()}? PixCut removes image backgrounds instantly with AI. Free to start, bulk up to 20 images, no install."
    canon  = f"{slug}.html"
    faq_pairs=[
        (f"Can PixCut handle {keyword.lower()}?",
         f"Yes &#8212; PixCut is built for {keyword.lower()}. AI removes backgrounds from any image instantly. "
         "Free to start, bulk processing up to 20 images, object remover and 8x upscaler included."),
        ("Is PixCut free?",
         "Yes &#8212; PixCut has a free tier with background removal and standard resolution downloads. "
         "HD downloads and bulk processing require a paid plan."),
        ("Does PixCut need installation?",
         "No &#8212; PixCut is web-based. Works in any browser on any device. No download or install required. "
         "iOS and Android apps also available."),
    ]
    bc_s=BC_SCHEMA([("Home",""),("All Topics","keywords.html"),(keyword,"")])
    fq_s=FAQ_SCHEMA(faq_pairs)
    body=cat_deep(cat,keyword)
    same=[k for k in KEYWORDS if k["cat"]==cat and k["slug"]!=slug][:6]
    links=" &#183; ".join(f'<a href="{BASE_PATH}/{r["slug"]}.html">{r["keyword"]}</a>' for r in same)

    return (HEAD(title,desc,canon,bc_s+fq_s)
        +"\n<body>\n"
        +f"<style>:root{{--ha:{a1};--hb:{a2};--fa:rgba(0,0,0,.05)}}</style>\n"
        +NAV()+"\n"
        +BC([("Home",BASE_PATH+"/"),("All Topics",BASE_PATH+"/keywords.html"),(keyword,"")])
        +'\n<section class="hero">'
        +f'\n  <div class="eyebrow">&#10022; {cat.replace("-"," ").title()}</div>'
        +f'\n  <h1><em>{keyword}</em><br>&#8212; With PixCut</h1>'
        +'\n  <p class="hsub">AI-powered &#183; Instant results &#183; Free to start &#183; Bulk 20 images &#183; No install</p>'
        +'\n  <div class="btns">'
        +f'\n    <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +f'\n    <a href="{BASE_PATH}/how-it-works.html" class="btn-s">How It Works</a>'
        +'\n  </div>'
        +'\n  <div class="stats">'
        +'\n    <div><span class="stat-n">AI</span><span class="stat-l">Powered</span></div>'
        +'\n    <div><span class="stat-n">Instant</span><span class="stat-l">Results</span></div>'
        +'\n    <div><span class="stat-n">Bulk 20</span><span class="stat-l">Images at Once</span></div>'
        +'\n    <div><span class="stat-n">Free</span><span class="stat-l">To Start</span></div>'
        +'\n  </div>\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">All Features</div><h2>Everything in PixCut</h2>'
        +FEATURES_GRID()
        +'\n</div></section>\n'
        +body
        +'\n<section style="background:#faf5ff"><div class="container"><div class="sec-ey">Real Users</div><h2>What People Say About PixCut</h2>'
        +TESTIMONIALS_GRID()
        +'\n</div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">FAQ</div><h2>Common Questions</h2>'
        +FAQ_BLOCK(faq_pairs+FAQ_GLOBAL[:3])
        +f'\n  <div style="margin-top:1.5rem"><a href="{BASE_PATH}/faq.html" style="color:var(--ha);font-weight:600;font-size:.88rem">View all FAQs &#8594;</a></div>'
        +'\n</div></section>\n'
        +'\n<section class="dark-sec"><div class="container"><div class="sec-ey">Related Topics</div><h2>Explore More</h2>'
        +related_cloud(kw_data,28)
        +(f'\n  <p style="margin-top:1.4rem;font-size:.78rem;color:rgba(255,255,255,.35)">More: {links}</p>' if links else '')
        +'\n</div></section>\n'
        +CTA(f"Try PixCut for {keyword.title()} &#8212; Free","AI-powered, instant, no installation required.")
        +"\n"+FOOTER()+"\n"+FAQ_JS+"\n</body></html>")


def page_index():
    extra=FAQ_SCHEMA(FAQ_GLOBAL[:6])+BC_SCHEMA([("Home","")])
    uses=[
        ("&#9986;","Remove Background",  "remove-background-from-image",     "Any image, instant AI"),
        ("&#128230;","Bulk Removal",      "bulk-background-remover",          "Up to 20 images at once"),
        ("&#128247;","Remove Objects",    "remove-object-from-photo",         "Watermarks, text, defects"),
        ("&#128200;","Upscale 8x",        "image-upscaler-online",            "No quality loss"),
        ("&#128736;","Product Photos",    "product-photo-background-remove",  "White ecommerce backgrounds"),
        ("&#129312;","AI Headshots",      "ai-headshot-generator",            "Selfie to LinkedIn photo"),
        ("&#127800;","Logo Transparent",  "logo-background-remover",          "Clean transparent PNG"),
        ("&#127760;","Developer API",     "background-remover-api-developers","Integrate into your app"),
    ]
    ug="".join(f'<a class="uc-card" href="{BASE_PATH}/{s}.html"><span class="uc-icon">{i}</span><span class="uc-label">{n}</span><span class="uc-sub">{d}</span></a>' for i,n,s,d in uses)
    return (HEAD(f"PixCut &#8212; AI Background Remover | Bulk, Upscale, Headshots | {YEAR}",
                 "AI removes image backgrounds in seconds. Bulk process 20 images, remove watermarks, upscale 8x, AI headshots. Free to start.",
                 "",extra)
        +"\n<body>\n"+NAV()
        +'\n<section class="hero">'
        +'\n  <div class="eyebrow">&#10022; AI Background Remover &#183; Free to Start</div>'
        +'\n  <h1>Remove Backgrounds.<br><em>Instantly. Accurately.</em></h1>'
        +'\n  <p class="hsub">AI removes image backgrounds in seconds. Bulk process up to 20 images, remove watermarks and objects, upscale up to 8x and generate AI headshots. No install, free to start.</p>'
        +'\n  <div class="btns">'
        +f'\n    <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +f'\n    <a href="{BASE_PATH}/how-it-works.html" class="btn-s">How It Works</a>'
        +'\n  </div>'
        +'\n  <div class="stats">'
        +'\n    <div><span class="stat-n">AI</span><span class="stat-l">Powered</span></div>'
        +'\n    <div><span class="stat-n">Bulk 20</span><span class="stat-l">Images at Once</span></div>'
        +'\n    <div><span class="stat-n">8x</span><span class="stat-l">Image Upscale</span></div>'
        +'\n    <div><span class="stat-n">Free</span><span class="stat-l">To Start</span></div>'
        +'\n  </div>\n</section>\n'
        +'\n<section style="background:#fff"><div class="container">'
        +'\n  <div class="sec-ey">What Do You Need?</div><h2>Every Image Task &#8212; Covered</h2>'
        +f'\n  <div class="uc-grid">{ug}</div>'
        +'\n</div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">Full Feature Suite</div>'
        +'\n  <h2>Background Removal Is Just the Start</h2>'
        +FEATURES_GRID()
        +f'\n  <div style="margin-top:2.5rem;text-align:center"><a href="{BASE_PATH}/features.html" style="color:var(--ha);font-weight:600">View full feature list &#8594;</a></div>'
        +'\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">Why PixCut?</div>'
        +'\n  <h2>Better Than Photoshop for Background Removal</h2>'
        +'\n  <div class="grid3">'
        +'\n    <div class="card"><div class="fi">&#128640;</div><h3>Seconds, Not Hours</h3><p>Photoshop background removal takes 5-15 minutes per image even for skilled editors. PixCut AI processes the same image in under 10 seconds &#8212; 50-100x faster.</p></div>'
        +'\n    <div class="card"><div class="fi">&#129504;</div><h3>Zero Skill Required</h3><p>Photoshop masking takes years to master. PixCut requires zero skill &#8212; upload an image, download the result. Anyone produces professional-quality cutouts.</p></div>'
        +'\n    <div class="card"><div class="fi">&#128185;</div><h3>Free to Start</h3><p>No subscription required to try. Remove backgrounds and download standard resolution images free. Upgrade for HD and bulk processing.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#faf5ff"><div class="container"><div class="sec-ey">Real Users</div>'
        +'\n  <h2 style="text-align:center;margin-bottom:2.5rem">Sellers, Designers &amp; Creators</h2>'
        +TESTIMONIALS_GRID()
        +'\n</div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">FAQ</div><h2>Common Questions</h2>'
        +FAQ_BLOCK(FAQ_GLOBAL[:6])
        +f'\n  <div style="margin-top:1.5rem;text-align:center"><a href="{BASE_PATH}/faq.html" style="color:var(--ha);font-weight:600">View all FAQs &#8594;</a></div>'
        +'\n</div></section>\n'
        +CTA()+"\n"+FOOTER()+"\n"+FAQ_JS+"\n</body></html>")

def page_features():
    bc=BC_SCHEMA([("Home",""),("Features","")])
    rows=[
        ("AI Background Removal",        "V","V","V","V","V"),
        ("Bulk Removal (20 images)",     "V","V","Partial","V","Paid"),
        ("Hair/Fine Detail Accuracy",    "V","V","V","Partial","V"),
        ("Object/Watermark Remover",     "V","X","X","X","Paid"),
        ("Image Upscaler (8x)",          "V","X","X","X","X"),
        ("AI Headshot Generator",        "V","X","X","X","X"),
        ("Background Replacer",          "V","Partial","V","V","Paid"),
        ("Developer API",                "V","V","X","V","Paid"),
        ("Mobile App",                   "V","V","V","V","V"),
        ("No Install Needed",            "V","V","V","V","V"),
        ("Free Tier with Downloads",     "V","Limited","V","V","X"),
    ]
    tools=["PixCut &#10022;","Remove.bg","Canva Pro","Adobe Express","Photoshop"]
    hrow="<tr><th>Feature</th>"+"".join(('<th class="hl">' if i==0 else '<th>')+t+'</th>' for i,t in enumerate(tools))+"</tr>"
    def cell(v,i):
        if i==0: return f'<td class="ck" style="font-weight:700">{v}</td>'
        if v=="V": return '<td class="ck">&#10004;</td>'
        if v=="X": return '<td class="cr">&#10008;</td>'
        return f'<td class="cp">{v}</td>'
    trows="".join("<tr>"+cell(r[0],-1)+"".join(cell(v,i) for i,v in enumerate(r[1:]))+"</tr>" for r in rows)
    return (HEAD(f"PixCut Features &#8212; Background Removal, Upscaler, AI Headshots | {YEAR}",
                 "Complete PixCut feature list vs Remove.bg, Canva Pro, Adobe Express and Photoshop.",
                 "features.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Features","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Complete Feature List</div>'
        +'\n  <h1>Everything PixCut<br><em>Can Do</em></h1>'
        +'\n  <p class="hsub">Background removal &#183; Bulk &#183; Object remove &#183; 8x upscale &#183; AI headshots &#8212; all free to start</p>'
        +f'\n  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">All Features</div><h2>The Complete Toolkit</h2>'
        +FEATURES_GRID()
        +'\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">5-Tool Comparison</div><h2>PixCut vs Every Alternative</h2>'
        +f'\n  <div class="tbl-wrap"><table><thead>{hrow}</thead><tbody>{trows}</tbody></table></div>'
        +'\n  <p style="margin-top:.9rem;font-size:.75rem;color:var(--muted)">&#10004; Full &#160; Partial = Limited &#160; &#10008; Not available</p>'
        +'\n</div></section>\n'
        +CTA("Try All Features Free","No credit card, no installation required.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_how_it_works():
    bc=BC_SCHEMA([("Home",""),("How It Works","")])
    return (HEAD(f"How PixCut Works &#8212; Remove Image Backgrounds in 3 Steps | {YEAR}",
                 "Remove image backgrounds with PixCut in 3 steps: upload, AI removes, download. Free, instant, no install.",
                 "how-it-works.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("How It Works","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Simple &amp; Instant</div>'
        +'\n  <h1>Remove Backgrounds in<br><em>3 Steps</em></h1>'
        +'\n  <p class="hsub">Upload &#8594; AI removes background &#8594; download transparent PNG. Done in seconds, free to start.</p>'
        +f'\n  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">Single Image</div><h2>3 Steps to Remove a Background</h2>'
        +'\n  <div class="steps">'
        +'\n    <div class="step"><div class="sn">1</div><h3>Upload Your Image</h3><p>Drag and drop, click Upload, or paste a URL. Supports JPG, PNG, WebP and other common formats. Works on any device in any browser.</p></div>'
        +'\n    <div class="step"><div class="sn">2</div><h3>AI Removes Background</h3><p>PixCut AI identifies the subject, traces the edges including hair and fine detail, and removes the background automatically. Under 10 seconds.</p></div>'
        +'\n    <div class="step"><div class="sn">3</div><h3>Download or Replace</h3><p>Download the transparent PNG, or replace the background with a solid colour, custom image or from PixCut\'s background library.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">Batch Mode</div><h2>Remove Backgrounds from 20 Images at Once</h2>'
        +'\n  <div class="steps">'
        +'\n    <div class="step"><div class="sn">1</div><h3>Upload Batch</h3><p>Select the Batch tab and upload up to 20 images. Mix product types, photo styles and image formats in the same batch.</p></div>'
        +'\n    <div class="step"><div class="sn">2</div><h3>AI Processes All</h3><p>All 20 images processed in parallel by PixCut AI. Complete results ready within 1-2 minutes.</p></div>'
        +'\n    <div class="step"><div class="sn">3</div><h3>Download All</h3><p>Download each image individually or all at once as a ZIP file. Ready to use immediately.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container" style="padding-top:0"><div class="sec-ey">Fine-Tune</div><h2>Manual Refinement Tools</h2>'
        +'\n  <div class="grid2">'
        +'\n    <div class="card"><div class="fi">&#9986;</div><h3>Erase Brush</h3><p>Remove any remaining background area the AI kept. Precise brush control for any areas needing manual cleanup after the AI pass.</p></div>'
        +'\n    <div class="card"><div class="fi">&#128396;</div><h3>Restore Brush</h3><p>Recover any subject area accidentally included in the background removal. Brings back any detail the AI removed that should remain.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#faf5ff"><div class="container"><div class="sec-ey">Real Results</div><h2>What Users Create</h2>'
        +TESTIMONIALS_GRID()
        +'\n</div></section>\n'
        +CTA("Try PixCut Free Now","No credit card, no installation. Start in seconds.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_faq():
    all_faqs=FAQ_GLOBAL+[
        ("Does PixCut work on logos?","Yes &#8212; PixCut accurately removes backgrounds from logos including complex illustrated logos with fine detail. Output is a transparent PNG with clean edges."),
        ("Can PixCut handle transparent or glass objects?","PixCut handles semi-transparent objects with good accuracy. Pure glass or completely transparent products remain challenging for all background removal AI. For most common cases, results are good."),
        ("Is PixCut good for ecommerce product photos?","Yes &#8212; PixCut is used widely for ecommerce. Bulk background removal, accurate white background replacement and precise edges on complex products make it a standard tool for Amazon, Shopify and Etsy sellers."),
        ("Can I use PixCut results for commercial use?","Yes &#8212; images processed with PixCut can be used for commercial purposes including product listings, marketing and print materials."),
        ("What image formats does PixCut support?","PixCut supports JPG, PNG, WebP and other common image formats. Output is always transparent PNG."),
        ("Does PixCut store my images?","PixCut stores uploaded images temporarily for processing. According to Wondershare's privacy policy, images are not used for training or shared with third parties."),
    ]
    fq=FAQ_SCHEMA(all_faqs)
    bc=BC_SCHEMA([("Home",""),("FAQ","")])
    return (HEAD(f"PixCut FAQ &#8212; {len(all_faqs)} Questions Answered | {YEAR}",
                 "Every PixCut question answered &#8212; background removal, bulk, ecommerce, upscaler, headshots and pricing.",
                 "faq.html",fq+bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("FAQ","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Complete FAQ</div>'
        +f'\n  <h1>Every PixCut Question<br><em>Answered</em></h1>'
        +f'\n  <p class="hsub">{len(all_faqs)} questions &#8212; background removal, bulk, ecommerce, upscaler and pricing.</p>'
        +'\n</section>\n'
        +f'\n<section><div class="container"><div class="sec-ey">All {len(all_faqs)} Questions</div><h2>Complete FAQ</h2>'
        +FAQ_BLOCK(all_faqs)
        +'\n</div></section>\n'
        +CTA("Ready to Try PixCut? It\'s Free","No credit card, no installation required.")
        +"\n"+FOOTER()+"\n"+FAQ_JS+"\n</body></html>")

def page_compare():
    bc=BC_SCHEMA([("Home",""),("Compare","")])
    comps=[
        ("vs Remove.bg","Remove.bg is the best-known background remover with strong accuracy. PixCut matches its core removal quality and adds: object and watermark removal, image upscaler to 8x, AI headshot generator and background replacer &#8212; all features Remove.bg lacks. PixCut's free tier is also more generous. For users needing more than background removal alone, PixCut is the more complete solution."),
        ("vs Canva Background Remover","Canva Pro's background remover requires a $13+/month subscription and only works inside Canva's design editor. PixCut works standalone on any image, handles complex subjects &#8212; especially hair &#8212; with better accuracy, and doesn't require a design subscription."),
        ("vs Adobe Photoshop","Photoshop produces excellent background removal but costs $21+/month, requires desktop installation and years of practice. PixCut produces comparable results in any browser in under 10 seconds, free of charge, with zero learning curve. For background removal specifically, PixCut is faster and more accessible for most users."),
        ("vs Other Free Tools","Basic free tools use colour selection algorithms that fail on complex backgrounds and fine detail. PixCut uses AI trained on millions of images &#8212; dramatically better results especially for hair, transparent objects and cluttered scenes."),
    ]
    comp_cards="".join(f'<div class="card"><h3>{n}</h3><p style="font-size:.87rem;color:var(--muted)">{d}</p></div>' for n,d in comps)
    return (HEAD(f"PixCut vs Remove.bg, Canva &amp; Photoshop &#8212; Best Background Remover {YEAR}",
                 "PixCut vs Remove.bg, Canva, Photoshop, Adobe Express. Honest AI background remover comparison 2025.",
                 "compare.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Compare","")])
        +f'\n<section class="hero"><div class="eyebrow">&#10022; Comparison {YEAR}</div>'
        +'\n  <h1>PixCut vs<br><em>Every Alternative</em></h1>'
        +'\n  <p class="hsub">Honest comparison &#8212; accuracy, features, pricing and free tier generosity.</p>'
        +f'\n  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +'\n</section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">Head-to-Head</div><h2>vs Every Alternative</h2>'
        +f'\n  <div class="grid2">{comp_cards}</div>'
        +'\n</div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">What PixCut Has Uniquely</div><h2>Three Features Others Don\'t Offer</h2>'
        +'\n  <div class="grid3">'
        +'\n    <div class="card"><div class="fi">&#128200;</div><h3>Image Upscaler to 8x</h3><p>Remove.bg, Canva and Photoshop have no AI upscaler built in. PixCut upscales to 8x original size &#8212; turning small thumbnails into full-resolution images usable for print.</p></div>'
        +'\n    <div class="card"><div class="fi">&#129312;</div><h3>AI Headshot Generator</h3><p>No major competitor includes an AI headshot generator. PixCut transforms a selfie into a professional LinkedIn-ready headshot &#8212; replacing a $200+ photography session.</p></div>'
        +'\n    <div class="card"><div class="fi">&#128247;</div><h3>Object &amp; Watermark Remover</h3><p>Remove.bg only removes backgrounds. PixCut also removes specific objects, watermarks, text and defects using AI content-aware fill &#8212; all in the same tool.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +CTA("The Most Complete Background Remover &#8212; Try Free","Download PixCut free &#8212; no credit card required.")
        +"\n"+FOOTER()+"\n</body></html>")

BLOG_POSTS=[
    {"slug":"remove-image-background-ai-guide","title":"How to Remove Image Backgrounds with AI in 2025","excerpt":"The fastest, most accurate way to remove any image background — AI tools compared.","cat":"Background Removal","read":"6 min","date":"2025-01-15",
     "body":"<h2>Why AI Background Removal Changed Everything</h2><p>Before AI tools, background removal required Photoshop masking skills that take years to develop, and 5-15 minutes per image even when mastered. AI background removal tools reduced this to under 10 seconds per image with no skill required. PixCut is one of the leading AI tools for this task.</p><h2>How PixCut Removes Backgrounds</h2><ol><li>Go to PixCut in any browser</li><li>Upload your image by dragging, clicking or pasting a URL</li><li>AI detects and removes the background automatically</li><li>Download the transparent PNG or replace the background</li></ol><h2>Best Use Cases</h2><p><strong>Product photos:</strong> White backgrounds for Amazon, Shopify and eBay. <strong>Profile photos:</strong> Neutral backgrounds for LinkedIn and company directories. <strong>Logos:</strong> Transparent PNG versions for use on any background. <strong>Graphic design:</strong> Isolated subjects for composite images and templates.</p>"},
    {"slug":"bulk-background-removal-ecommerce","title":"Bulk Background Removal for Ecommerce &#8212; Remove 20 Product Backgrounds at Once","excerpt":"Save hours every week removing backgrounds from product photos with bulk processing.","cat":"Bulk Processing","read":"7 min","date":"2025-02-10",
     "body":"<h2>The Ecommerce Photo Editing Problem</h2><p>Amazon, Shopify and most major marketplaces require product photos on pure white backgrounds. For sellers with large catalogues, creating these individually takes hours. PixCut's bulk processing handles 20 images simultaneously &#8212; transforming a multi-hour task into minutes.</p><h2>How Bulk Background Removal Works</h2><ol><li>Open PixCut and select the Batch tab</li><li>Upload up to 20 product images</li><li>AI processes all images in parallel</li><li>Download all with white backgrounds as a ZIP</li></ol><h2>What Gets Results</h2><p>For best results: use consistent lighting on source photos, ensure the product is the clear subject, and avoid backgrounds that match the product colour. PixCut AI handles the rest &#8212; including difficult product types like jewellery, clothing and glass.</p>"},
    {"slug":"product-photo-white-background-guide","title":"How to Create Professional Product Photos with White Backgrounds","excerpt":"Amazon-compliant product photos from any image — AI background removal guide for sellers.","cat":"Ecommerce","read":"6 min","date":"2025-03-05",
     "body":"<h2>Amazon's White Background Requirement</h2><p>Amazon's main product image rules: pure white background (RGB 255,255,255), product fills 85%+ of frame, no props or text. These requirements apply to all main product images. PixCut creates Amazon-compliant product photos in seconds.</p><h2>Steps</h2><ol><li>Upload product photo to PixCut</li><li>AI removes existing background</li><li>Select white as replacement background</li><li>Adjust product position if needed</li><li>Download the white background image</li></ol><h2>For Difficult Products</h2><p>Jewellery (fine chains, small details), clothing (thin fabric, lace), glass (transparent), electronics (shiny reflective surfaces) &#8212; all supported by PixCut's AI. The accuracy on complex edges is significantly better than basic selection tools.</p>"},
    {"slug":"ai-headshot-generator-guide","title":"AI Headshot Generator &#8212; Professional Headshot from a Selfie","excerpt":"Transform a regular selfie into a professional LinkedIn headshot using PixCut's AI headshot generator.","cat":"AI Headshots","read":"5 min","date":"2025-04-12",
     "body":"<h2>Why Professional Headshots Matter</h2><p>LinkedIn profiles with professional photos receive significantly more connection requests and profile views than those with casual photos. Professional headshot sessions cost $200-500+. PixCut's AI Headshot Generator produces professional-quality headshots from a regular selfie.</p><h2>How It Works</h2><ol><li>Upload a clear selfie to PixCut</li><li>Select AI Headshot Generator</li><li>Choose a headshot style (business, creative, academic)</li><li>AI transforms the photo with professional lighting and background</li><li>Download your professional headshot</li></ol><h2>Tips for Best Results</h2><p>Use a selfie with good, even lighting (natural light works well). Face the camera directly. Clear expression. The AI handles background removal, colour grading, lighting adjustment and professional styling.</p>"},
    {"slug":"remove-watermark-from-image-guide","title":"How to Remove Watermarks from Images Online","excerpt":"Remove watermarks, text and defects from photos using PixCut's AI object remover.","cat":"Object Removal","read":"5 min","date":"2025-05-20",
     "body":"<h2>When You Need Watermark Removal</h2><p>Old product images with watermarks. Draft images with trial watermarks. Photos of physical products with price tag stickers. Documents with unwanted text stamps. PixCut's object remover handles all of these using AI content-aware fill.</p><h2>How It Works</h2><ol><li>Upload the image to PixCut</li><li>Select Object Remover</li><li>Paint over the watermark with the brush tool</li><li>Adjust brush size to cover the watermark precisely</li><li>AI fills the area with matching surrounding content</li><li>Download the cleaned image</li></ol><h2>Content-Aware Fill</h2><p>Unlike simple blurring or blocking out, PixCut's content-aware fill analyses surrounding pixels and fills the removed area with plausible matching content. The result is invisible &#8212; no obvious patch or blurred area.</p>"},
    {"slug":"upscale-image-without-quality-loss","title":"How to Upscale Images Without Quality Loss &#8212; AI Upscaler Guide","excerpt":"Make small images larger without blurring — AI upscaling adds genuine detail up to 8x.","cat":"Image Enhancement","read":"6 min","date":"2025-06-15",
     "body":"<h2>Why Regular Upscaling Creates Blurry Images</h2><p>Traditional upscaling simply stretches pixels &#8212; making them larger but not sharper. The result is a bigger image that looks blurry or pixelated. AI upscaling is fundamentally different: the AI adds plausible detail based on training data from millions of high-quality images, producing a genuinely sharper larger image.</p><h2>PixCut Image Upscaler</h2><ol><li>Upload your low-resolution image to PixCut</li><li>Select Image Upscaler</li><li>Choose upscale factor (2x, 4x or 8x)</li><li>AI enhances and upscales the image</li><li>Download the high-resolution result</li></ol><h2>Use Cases</h2><p>Old product photos at lower resolution. Thumbnails needing to be enlarged for display. Images compressed heavily for web use. Scanned photos at limited resolution. Profile pictures needing enlargement for print use.</p>"},
    {"slug":"pixcut-vs-remove-bg-comparison","title":"PixCut vs Remove.bg &#8212; Which AI Background Remover Is Better in 2025?","excerpt":"Both use AI to remove backgrounds, but they're very different tools. Honest comparison.","cat":"Compare","read":"7 min","date":"2025-07-10",
     "body":"<h2>Background Removal Quality</h2><p>Both PixCut and Remove.bg produce high-quality AI background removal. Edge accuracy on hair, fur and fine detail is comparable between the two tools. Both outperform manual selection tools and older algorithm-based removers significantly.</p><h2>Where PixCut Has More</h2><p><strong>Object/watermark remover:</strong> Remove.bg only removes backgrounds. PixCut also removes objects, watermarks and defects. <strong>Image upscaler to 8x:</strong> Remove.bg has no upscaler. <strong>AI headshot generator:</strong> Remove.bg has no headshot feature. <strong>Background replacer:</strong> Both have this, but PixCut's library is larger.</p><h2>Free Tier Comparison</h2><p>PixCut's free tier allows more free background removal downloads than Remove.bg's limited free quota. Both have paid plans for HD downloads and bulk processing.</p><h2>Verdict</h2><p>For pure background removal only, both tools are comparable in quality. For users who also need object removal, upscaling or AI headshots &#8212; PixCut is the more complete solution.</p>"},
    {"slug":"background-remover-ecommerce-sellers","title":"Best Background Remover for Ecommerce Sellers in 2025","excerpt":"Every major marketplace requires clean white backgrounds. Here's the fastest way to meet the requirement.","cat":"Ecommerce","read":"7 min","date":"2025-08-05",
     "body":"<h2>Marketplace Background Requirements</h2><p>Amazon: pure white (RGB 255,255,255), product fills 85%+ of frame. eBay: white or light background recommended. Shopify: consistent clean backgrounds recommended for stores. Etsy: clean backgrounds that show product clearly. PixCut meets all of these requirements automatically.</p><h2>Why PixCut Is the Right Tool</h2><p>Bulk processing up to 20 images simultaneously. Accurate AI that handles jewellery, clothing, glass and other difficult products. One-click white background replacement. Consistent results across an entire catalogue. Significant time saving vs Photoshop or manual tools.</p><h2>Workflow for Large Catalogues</h2><ol><li>Photograph products consistently (same setup, consistent lighting)</li><li>Upload 20 at a time to PixCut batch mode</li><li>AI removes backgrounds, apply white replacement</li><li>Download batch as ZIP</li><li>Repeat for next 20</li><li>200 product images = 10 batches = approximately 30 minutes total</li></ol>"},
    {"slug":"transparent-png-background-guide","title":"How to Make a PNG with Transparent Background Online Free","excerpt":"Create transparent PNG images from any photo — for logos, graphics, overlays and design.","cat":"Background Removal","read":"5 min","date":"2025-09-15",
     "body":"<h2>What Is a Transparent PNG?</h2><p>A PNG with a transparent background shows the image subject with no background &#8212; the background area is transparent rather than a colour. When placed on any background in a design tool, the subject appears to float naturally on that background.</p><h2>When You Need Transparent PNGs</h2><ul><li>Logo files for use on any website background colour</li><li>Product images for design templates</li><li>Subject images for photo composites</li><li>Overlay images for video thumbnails</li><li>Stickers and graphics for social media</li></ul><h2>Create Transparent PNG with PixCut</h2><ol><li>Upload your image to PixCut</li><li>AI removes the background automatically</li><li>Download as PNG &#8212; the file has a transparent background</li><li>Open in any design tool and place on any background</li></ol>"},
    {"slug":"logo-background-removal-guide","title":"How to Remove Background from a Logo Online Free","excerpt":"Turn any logo into a transparent PNG — for websites, business cards, presentations and more.","cat":"Design & Marketing","read":"5 min","date":"2025-10-20",
     "body":"<h2>Why Logos Need Transparent Backgrounds</h2><p>A logo on a white square looks unprofessional on a coloured website header. A logo PNG with transparent background works on any background &#8212; white, dark, coloured, photographic. Most logos are delivered on white backgrounds and need to be converted to transparent for professional use.</p><h2>Steps with PixCut</h2><ol><li>Upload the logo image to PixCut</li><li>AI removes the white or coloured background</li><li>Download as transparent PNG</li><li>Use on any background in any design tool</li></ol><h2>Complex Logos</h2><p>Logos with fine detail, gradient fills, drop shadows or illustrated elements &#8212; PixCut handles all of these. For logos with semi-transparent elements (drop shadows, glows), the transparency is preserved accurately in the output PNG.</p>"},
    {"slug":"pixcut-for-photographers","title":"PixCut for Photographers &#8212; Background Removal at Professional Scale","excerpt":"How professional photographers use PixCut to deliver clean isolated images at scale.","cat":"Use Cases","read":"6 min","date":"2025-11-10",
     "body":"<h2>The Photographer Use Case</h2><p>Portrait photographers need clean background removal for studio composites. Product photographers need white or transparent backgrounds for commercial clients. Real estate photographers remove distracting elements from property photos. PixCut handles all three scenarios.</p><h2>Portrait Photography Workflows</h2><p>Upload portrait batches to PixCut. AI removes studio backgrounds for composite backgrounds or neutral white. Manually refine any hair or edge details with the restore/erase brush. Download isolated portrait PNGs ready for composite into any background or template.</p><h2>Product Photography Delivery</h2><p>Commercial clients typically want both white-background versions (for ecommerce) and isolated transparent versions (for marketing use). PixCut produces both in one session &#8212; remove background, download the transparent PNG, then apply white background, download again. Two deliverable formats in under a minute per image.</p>"},
    {"slug":"how-to-change-photo-background-online","title":"How to Change a Photo Background Online Free","excerpt":"Remove one background and add another — the complete guide to background replacement.","cat":"Background Removal","read":"5 min","date":"2025-12-01",
     "body":"<h2>Background Replacement Process</h2><p>Changing a photo background involves two steps: removing the original background and adding a new one. PixCut handles both steps in the same tool.</p><h2>Steps</h2><ol><li>Upload your photo to PixCut</li><li>AI removes the original background</li><li>Click Replace Background</li><li>Choose from solid colours, PixCut's background library, or upload your own</li><li>Preview the result</li><li>Download the final image</li></ol><h2>Background Options</h2><p><strong>Solid colours:</strong> White (for products), black (for dramatic portraits), any HEX colour. <strong>PixCut library:</strong> Nature scenes, office settings, studio backgrounds, seasonal themes. <strong>Your own image:</strong> Upload any background image &#8212; a specific room, location, branded backdrop or any photo.</p>"},
    {"slug":"best-ai-background-remover-2025","title":"Best AI Background Remover 2025 &#8212; Ranked &amp; Reviewed","excerpt":"We tested every major AI background remover. Here's the honest ranking for 2025.","cat":"Compare","read":"8 min","date":"2026-01-15",
     "body":"<h2>How We Evaluated</h2><p>We tested: accuracy on hair and fine detail, speed, bulk processing, additional features, pricing and free tier generosity across all major AI background removal tools.</p><h2>1. Wondershare PixCut &#8212; Best Overall</h2><p>Excellent background removal accuracy. Bulk processing up to 20 images. Object and watermark remover. 8x image upscaler. AI headshot generator. Background replacer. Developer API. Free tier available. <strong>Best choice for most users.</strong></p><h2>2. Remove.bg &#8212; Best Background-Only Tool</h2><p>Excellent accuracy comparable to PixCut. No object remover, no upscaler, no headshot generator. More limited free tier. <strong>Good if you only ever need background removal.</strong></p><h2>3. Canva Pro &#8212; Best for Canva Users</h2><p>Convenient if you're already in Canva. Less accurate on complex subjects. Requires Canva Pro subscription. No standalone access. <strong>Use if you're already a Canva Pro subscriber.</strong></p><h2>Recommendation</h2><p>For any use case beyond pure background removal &#8212; or for the most complete tool &#8212; PixCut is the clear winner in 2025.</p>"},
    {"slug":"pixcut-for-social-media","title":"PixCut for Social Media &#8212; Create Professional Images Fast","excerpt":"Remove backgrounds, create consistent visual styles and produce professional social media content at scale.","cat":"Design & Marketing","read":"6 min","date":"2026-02-10",
     "body":"<h2>Social Media Image Requirements</h2><p>Instagram, LinkedIn, TikTok and YouTube thumbnails all perform better with professional, clean visuals. Isolated subjects on branded backgrounds, consistent colour schemes, and high-quality product or portrait images &#8212; all are achievable with PixCut in minutes.</p><h2>Common Social Media Uses</h2><p><strong>Instagram product posts:</strong> Isolated products on white, gradient or colour backgrounds. <strong>LinkedIn banners:</strong> Professional headshot with branded background. <strong>YouTube thumbnails:</strong> Isolated person or product with text overlaid on clean background. <strong>TikTok backgrounds:</strong> Remove distracting home backgrounds from talking head videos.</p><h2>Batch Workflow for Content Creators</h2><p>Upload 20 images in batch mode &#8212; product photos, portraits, lifestyle shots. Remove all backgrounds at once. Apply consistent branded backgrounds using PixCut's replacer. Download the batch. Upload to your scheduling tool. A week's worth of consistent, professional social content in one session.</p>"},
    {"slug":"free-background-remover-no-watermark","title":"Free Background Remover Without Watermarks &#8212; PixCut vs Others","excerpt":"Which background removers add watermarks to free downloads? PixCut vs Remove.bg vs Canva compared.","cat":"Background Removal","read":"5 min","date":"2026-03-05",
     "body":"<h2>The Watermark Problem</h2><p>Many free background removers add a watermark to downloaded images on the free tier &#8212; forcing an upgrade to get a clean file. PixCut does not add watermarks to free background removal downloads. Standard resolution images download clean on the free plan.</p><h2>What's Free vs Paid with PixCut</h2><p><strong>Free:</strong> Background removal, standard resolution download (no watermark), object remover (limited), background replacer. <strong>Paid:</strong> HD resolution downloads, bulk processing more than a few images, higher object removal quota, unlimited access.</p><h2>Comparison</h2><p>Remove.bg: watermark on free downloads unless upgraded. Canva: watermark on free downloads for Pro features. PixCut: standard resolution downloads clean on free plan. For users who only occasionally need background removal, PixCut's free tier provides genuine usable output without needing to upgrade.</p>"},
]

def page_blog():
    bc=BC_SCHEMA([("Home",""),("Blog","")])
    cards="".join(
        f'<div class="card"><div class="badge">{p["cat"]}</div>'
        f'<h3 style="margin-top:.55rem;margin-bottom:.45rem;font-size:.97rem">'
        f'<a href="{BASE_PATH}/blog/{p["slug"]}.html" style="color:var(--ink)">{p["title"]}</a></h3>'
        f'<p style="font-size:.84rem;margin-bottom:.85rem">{p["excerpt"]}</p>'
        f'<div style="display:flex;justify-content:space-between;align-items:center">'
        f'<span style="font-size:.73rem;color:var(--muted)">{p["date"]} &#183; {p["read"]}</span>'
        f'<a href="{BASE_PATH}/blog/{p["slug"]}.html" style="font-size:.8rem;font-weight:600;color:var(--ha)">Read &#8594;</a>'
        f'</div></div>'
        for p in BLOG_POSTS)
    return (HEAD(f"PixCut Blog &#8212; Background Removal Guides &amp; Tutorials | {YEAR}",
                 "AI background removal guides — ecommerce, portraits, bulk processing, upscaling and design tutorials.",
                 "blog.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Blog","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Background Removal Guides</div>'
        +f'\n  <h1>Guides &amp;<br><em>Tutorials</em></h1>'
        +f'\n  <p class="hsub">{len(BLOG_POSTS)} in-depth articles for every PixCut use case.</p>'
        +'\n</section>\n'
        +f'\n<section><div class="container"><div class="sec-ey">All {len(BLOG_POSTS)} Articles</div><h2>Background Removal Guides</h2>'
        +f'\n  <div class="grid3">{cards}</div>'
        +'\n</div></section>\n'
        +CTA("Ready to Remove Backgrounds?","Try PixCut free &#8212; no credit card required.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_blog_post(post):
    bc=BC_SCHEMA([("Home",""),("Blog","blog.html"),(post["title"][:40]+"...","")])
    art=ART_SCHEMA(post["title"],post["excerpt"],post["date"])
    others=[p for p in BLOG_POSTS if p["slug"]!=post["slug"]][:3]
    rel="".join(f'<div class="card"><div class="badge">{p["cat"]}</div><h3 style="margin-top:.5rem;font-size:.93rem"><a href="{BASE_PATH}/blog/{p["slug"]}.html" style="color:var(--ink)">{p["title"]}</a></h3><p style="font-size:.82rem">{p["excerpt"]}</p></div>' for p in others)
    h=HEAD(f'{post["title"]} | PixCut Guide',post["excerpt"],f'blog/{post["slug"]}.html',bc+art,"article")
    return (h+"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Blog",BASE_PATH+"/blog.html"),(post["cat"],"")])
        +'\n<section class="hero" style="padding:3.5rem clamp(1rem,5vw,3rem) 3rem">'
        +f'\n  <div class="eyebrow">&#10022; {post["cat"]} &#183; {post["read"]}</div>'
        +f'\n  <h1 style="font-size:clamp(1.7rem,4vw,2.8rem)">{post["title"]}</h1>'
        +f'\n  <p class="hsub" style="font-size:1rem">{post["excerpt"]}</p>'
        +f'\n  <p style="color:rgba(255,255,255,.38);font-size:.76rem">Published {post["date"]}</p>'
        +'\n</section>\n'
        +'\n<section style="background:#fff"><div class="container"><div style="max-width:780px">'
        +f'\n  <div class="prose">{post["body"]}</div>'
        +f'\n  <div class="notice" style="margin-top:2.5rem"><strong>Try PixCut free.</strong> AI background removal, bulk processing and more. '
        +f'\n    <a href="{AFFILIATE_URL}" target="_blank" rel="nofollow sponsored" style="color:var(--ha);font-weight:600">Get started &#8594;</a>'
        +'\n  </div></div></div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">More Guides</div><h2>Related Articles</h2>'
        +f'\n  <div class="grid3">{rel}</div>'
        +'\n</div></section>\n'
        +CTA()+"\n"+FOOTER()+"\n</body></html>")

def page_glossary():
    terms=[
        ("Background Removal","The process of separating a photo subject from its background. AI tools like PixCut do this automatically in seconds."),
        ("Transparent Background","A PNG image where the background area is transparent (no colour) rather than white or coloured. Allows placement on any background in design tools."),
        ("PNG Format","Portable Network Graphics image format. Supports transparency, making it the standard output format for background-removed images."),
        ("AI Background Removal","Using machine learning to automatically detect and remove image backgrounds. More accurate and much faster than manual masking."),
        ("Content-Aware Fill","An AI technique that fills a removed area with content that plausibly matches surrounding pixels. Used in PixCut's object remover."),
        ("Bulk Processing","Removing backgrounds from multiple images simultaneously. PixCut handles up to 20 images in one batch."),
        ("Object Remover","A tool that removes specific objects, watermarks, text or defects from within a photo using content-aware fill."),
        ("Image Upscaling","Making an image larger. AI upscaling adds genuine detail rather than just stretching pixels, producing sharper larger images."),
        ("AI Headshot Generator","An AI tool that transforms a selfie into a professional-style headshot photo. PixCut's generator produces LinkedIn-quality headshots."),
        ("Background Replacer","A tool that adds a new background to an image after the original has been removed. PixCut supports solid colours, custom images and a background library."),
        ("Erase Brush","A manual tool in PixCut for removing background areas the AI kept after automatic removal. Precision manual cleanup."),
        ("Restore Brush","A manual tool in PixCut for recovering subject areas accidentally removed by the AI. Brings back detail mistakenly included in the background."),
        ("Edge Accuracy","How precisely the boundary between subject and background is detected during removal. High edge accuracy preserves natural details like hair without hard cutout edges."),
        ("HEIC Format","iPhone photo format. Not all tools accept HEIC &#8212; PixCut accepts HEIC images and converts to standard format during processing."),
        ("White Background Product Photo","A product photo on pure white (RGB 255,255,255) background. Required by Amazon and most major ecommerce platforms for main product images."),
        ("REST API","A programming interface that allows developers to integrate PixCut's background removal into their own applications or workflows via code."),
        ("Photomask","A selection mask defining which pixels belong to the subject and which to the background. AI tools generate masks automatically."),
        ("Feathered Edge","A soft, graduated edge between subject and background that looks natural. AI background removal creates feathered edges rather than hard cuts."),
        ("JPG/JPEG Format","Common compressed image format. PixCut accepts JPG input and can output as PNG (with transparency) after background removal."),
        ("Colour Background","A solid coloured background added after removal. Common in ecommerce for lifestyle images and in portraits for professional backgrounds."),
        ("Hair Masking","Background removal specifically around hair &#8212; the most technically challenging part of portrait removal. PixCut's AI handles complex hair accurately."),
        ("Commercial Use","Using PixCut's output images for business purposes including product listings, advertising and marketing materials. Permitted under PixCut's licensing terms."),
        ("WebP Format","Modern web image format with smaller file sizes. PixCut accepts WebP images for background removal processing."),
        ("Resolution","The number of pixels in an image (e.g. 1920x1080). PixCut's free tier supports standard resolution. Paid plans unlock HD high-resolution output."),
        ("Photo Enhancement","Improving overall image quality including sharpness, colour and exposure. PixCut's photo enhancer applies AI corrections automatically."),
    ]
    cards="".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t,d in terms)
    bc=BC_SCHEMA([("Home",""),("Glossary","")])
    return (HEAD(f"Background Removal Glossary &#8212; {len(terms)} Terms | {YEAR}",
                 "Complete background removal glossary &#8212; AI, transparent PNG, bulk processing, upscaling and more.",
                 "glossary.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Glossary","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Background Removal Reference</div>'
        +'\n  <h1>Background Removal<br><em>Glossary</em></h1>'
        +f'\n  <p class="hsub">{len(terms)} plain-language definitions for every image editing term.</p>'
        +'\n</section>\n'
        +f'\n<section><div class="container"><div class="sec-ey">{len(terms)} Terms</div><h2>Complete Glossary</h2>'
        +f'\n  <div class="grid3">{cards}</div>'
        +'\n</div></section>\n'
        +CTA("Ready to Remove Backgrounds?","Try PixCut free &#8212; no credit card required.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_download():
    bc=BC_SCHEMA([("Home",""),("Try Free","")])
    return (HEAD(f"Try PixCut Free &#8212; AI Background Remover Online | {YEAR}",
                 "Try Wondershare PixCut free. AI background removal, bulk processing, object remover, 8x upscaler. Free to start, no install.",
                 "download.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Try Free","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Free to Start</div>'
        +'\n  <h1>Try PixCut<br><em>Free Today</em></h1>'
        +'\n  <p class="hsub">AI background removal &#8212; free to start, no credit card, no installation. Works in any browser.</p>'
        +f'\n  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored" style="font-size:1.1rem;padding:1rem 2.5rem">&#8659; Try PixCut Free</a>'
        +'\n  <p style="color:rgba(255,255,255,.38);font-size:.78rem;margin-top:1rem">No installation &#183; Any browser &#183; Windows, Mac, Android, iOS</p>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">What\'s Included Free</div><h2>PixCut Free Tier</h2>'
        +FEATURES_GRID()
        +'\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">No Install Needed</div><h2>Works in Any Browser</h2>'
        +'\n  <div class="grid3">'
        +'\n    <div class="card"><h3>&#127760; Web Browser</h3><p>PixCut works in Chrome, Firefox, Safari, Edge and any modern browser. No download required. Open, upload, done.</p></div>'
        +'\n    <div class="card"><h3>&#128241; Mobile Apps</h3><p>iOS and Android apps available for on-the-go background removal. Same AI quality as the web version.</p></div>'
        +'\n    <div class="card"><h3>&#128736; Developer API</h3><p>Integrate PixCut into your own applications via the REST API. Documentation available for developers.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +CTA("Try PixCut Free Now","No credit card &#183; No installation &#183; Instant results.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_keywords():
    cats=defaultdict(list)
    for k in KEYWORDS: cats[k["cat"]].append(k)
    sections=""
    for cat in sorted(cats.keys()):
        items=cats[cat]; desc=CAT_DESC.get(cat,""); a1,_=ac(cat)
        links="".join(f'<a class="kw" href="{BASE_PATH}/{k["slug"]}.html">{k["keyword"]}</a>' for k in items)
        sections+=(f'<div style="margin-bottom:3rem"><h3 style="font-size:1rem;font-weight:700;color:{a1};margin-bottom:.35rem;border-bottom:2px solid {a1};padding-bottom:.35rem;display:inline-block">{cat.replace("-"," ").title()} <span style="color:var(--muted);font-weight:400;font-size:.83rem">({len(items)})</span></h3>'
                   +(f'<p style="font-size:.82rem;color:var(--muted);margin:.45rem 0 .7rem;max-width:600px">{desc}</p>' if desc else '')
                   +f'<div class="kw-cloud">{links}</div></div>')
    bc=BC_SCHEMA([("Home",""),("All Topics","")])
    return (HEAD(f"PixCut &#8212; All {len(KEYWORDS)} Topics | {YEAR}",
                 "Browse all PixCut topics &#8212; background removal, bulk, ecommerce, portraits, upscaling and more.",
                 "keywords.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("All Topics","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Topic Directory</div>'
        +'\n  <h1>All Background Removal<br><em>Topics</em></h1>'
        +f'\n  <p class="hsub">{len(KEYWORDS)} targeted topics for every PixCut use case.</p>'
        +'\n</section>\n'
        +f'\n<section><div class="container"><div class="sec-ey">Browse All {len(KEYWORDS)} Topics</div>{sections}</div></section>\n'
        +CTA()+"\n"+FOOTER()+"\n</body></html>")

def page_privacy():
    bc=BC_SCHEMA([("Home",""),("Privacy","")])
    return (HEAD("Privacy Policy &#8212; PixCut Guide","Privacy policy for PixCut affiliate guide website.","privacy.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Privacy Policy","")])
        +'\n<section class="hero" style="padding:3.5rem 2rem 3rem"><div class="eyebrow">Legal</div><h1>Privacy <em>Policy</em></h1></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="prose" style="max-width:800px">'
        +f'\n  <p><strong>Last updated: {BUILD_DATE}</strong></p>'
        +'\n  <h3>1. About</h3><p>Affiliate promotional site for Wondershare PixCut AI background remover. We do not collect personal data beyond standard server logs.</p>'
        +'\n  <h3>2. Affiliate Disclosure</h3><p>Links on this site are affiliate links. When you purchase via our links, we may earn a commission at no extra cost to you.</p>'
        +'\n  <h3>3. Cookies</h3><p>This website does not use tracking cookies.</p>'
        +'\n  <h3>4. External Links</h3><p>Purchase links go to the official Wondershare website. We are not responsible for external site privacy practices.</p>'
        +'\n</div></div></section>\n'+FOOTER()+"\n</body></html>")

def page_404():
    return (f"<!DOCTYPE html>\n<html lang=\"en\"><head>\n<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            f"<title>Page Not Found &#8212; PixCut</title>\n"
            f"<meta http-equiv=\"refresh\" content=\"4;url={SITE_DOMAIN}/\"/>\n"
            "<style>body{font-family:system-ui,sans-serif;background:#1e1b4b;color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;margin:0;padding:2rem}"
            "h1{font-size:3rem;margin-bottom:.75rem;font-weight:800}p{color:rgba(255,255,255,.6);margin-bottom:2rem;line-height:1.6}"
            "a{background:#7c3aed;color:#fff;padding:.85rem 2.2rem;border-radius:8px;text-decoration:none;font-weight:700}</style>"
            f"</head><body><div><div style=\"font-size:4rem;margin-bottom:1rem\">&#9986;</div><h1>Page Not Found</h1>"
            f"<p>Redirecting to homepage in 4 seconds...</p><a href=\"{SITE_DOMAIN}/\">Go to PixCut Home</a></div></body></html>")

def build_sitemap():
    essential=[("",1.0,"weekly"),("features.html",.9,"monthly"),("how-it-works.html",.9,"monthly"),
               ("faq.html",.85,"monthly"),("compare.html",.85,"monthly"),("blog.html",.85,"weekly"),
               ("download.html",.9,"monthly"),("keywords.html",.8,"monthly"),
               ("glossary.html",.75,"monthly"),("privacy.html",.3,"yearly")]
    urls=""
    for path,pri,freq in essential:
        loc=SITE_DOMAIN+("/"+path if path else "/")
        urls+=f"  <url><loc>{loc}</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>{freq}</changefreq><priority>{pri}</priority></url>\n"
    for p in BLOG_POSTS:
        urls+=f"  <url><loc>{SITE_DOMAIN}/blog/{p['slug']}.html</loc><lastmod>{p['date']}</lastmod><changefreq>monthly</changefreq><priority>0.75</priority></url>\n"
    for k in KEYWORDS:
        urls+=f"  <url><loc>{SITE_DOMAIN}/{k['slug']}.html</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>monthly</changefreq><priority>0.65</priority></url>\n"
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'</urlset>'

def build_robots():
    return f"User-agent: *\nAllow: /\nDisallow: /build-report.json\nSitemap: {SITE_DOMAIN}/sitemap.xml\n"

def build_llms():
    cats=sorted(set(k["cat"] for k in KEYWORDS))
    sample=", ".join(k["keyword"] for k in KEYWORDS[:30])
    return (f"# Wondershare PixCut\n\n"
            "> AI-powered online background remover. Removes backgrounds from any image automatically in seconds. Bulk processing up to 20 images, object and watermark remover, 8x image upscaler, AI headshot generator.\n\n"
            "## Key Features\n"
            "- AI background removal: instant, accurate, free to start\n"
            "- Bulk background removal: up to 20 images simultaneously\n"
            "- Object/watermark remover: AI content-aware fill\n"
            "- Image upscaler: up to 8x without quality loss\n"
            "- Background replacer: solid colour, custom or library\n"
            "- AI headshot generator: selfie to professional LinkedIn photo\n"
            "- Developer REST API\n"
            "- Web-based: no install, any browser, Windows/Mac/iOS/Android\n\n"
            "## Use Cases\n"
            "- Ecommerce product photos (Amazon, Shopify, eBay white background requirement)\n"
            "- Portrait and profile photo background removal\n"
            "- Logo and brand asset transparent PNG creation\n"
            "- Social media content and marketing images\n"
            "- Developer API integration for automated workflows\n\n"
            "## Pricing\nFree tier with standard resolution downloads. Paid plans for HD and bulk.\n\n"
            f"## Try Free\n{AFFILIATE_URL}\n\n"
            "## Developer\nWondershare Technology Co., Ltd.\n\n"
            f"## Site\n{SITE_DOMAIN}\n"
            f"{len(KEYWORDS)} keyword pages &#183; {len(BLOG_POSTS)} blog posts &#183; {len(cats)} categories\n"
            f"Sitemap: {SITE_DOMAIN}/sitemap.xml\n\n"
            f"## Categories\n{', '.join(c.title() for c in cats)}\n\n"
            f"## Sample Keywords\n{sample}\n")

WORKFLOW="""name: Build & Deploy PixCut

on:
  workflow_dispatch:

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Remove all old files from repo
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          find . -maxdepth 1 -type f ! -name 'build.py' ! -name 'README.md' -delete
          find . -maxdepth 1 -type d ! -name '.' ! -name '.git' ! -name '.github' -exec rm -rf {} + 2>/dev/null || true
          git add -A
          git diff --staged --quiet || git commit -m "Clean up old files"
          git push origin main

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Run build script
        run: python3 build.py

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""

def progress(i,total,label=""):
    pct=i/total; bar="█"*int(30*pct)+"░"*(30-int(30*pct))
    print(f"\r  [{bar}] {i:>4}/{total} {label:<42}",end="",flush=True)

def main():
    os.makedirs(DIST,exist_ok=True)
    os.makedirs(DIST+"/blog",exist_ok=True)
    os.makedirs(DIST+"/.github/workflows",exist_ok=True)

    print(f"\n{'═'*60}")
    print(f"  PixCut Site Builder — {BUILD_DATE}")
    print(f"{'═'*60}")
    print(f"  Domain:   {SITE_DOMAIN}")
    print(f"  Keywords: {len(KEYWORDS)}")
    print(f"  Blog:     {len(BLOG_POSTS)} posts")
    print(f"{'═'*60}\n")

    essential={
        "index.html":        page_index(),
        "features.html":     page_features(),
        "how-it-works.html": page_how_it_works(),
        "faq.html":          page_faq(),
        "compare.html":      page_compare(),
        "blog.html":         page_blog(),
        "download.html":     page_download(),
        "keywords.html":     page_keywords(),
        "glossary.html":     page_glossary(),
        "privacy.html":      page_privacy(),
        "404.html":          page_404(),
    }
    print("  Essential pages:")
    for fname,html in essential.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(html)
        print(f"    ✓ {fname}  ({len(html)//1024}KB)")

    print(f"\n  Blog posts ({len(BLOG_POSTS)}):")
    for post in BLOG_POSTS:
        with open(DIST+"/blog/"+post["slug"]+".html","w",encoding="utf-8") as f:
            f.write(page_blog_post(post))
        print("    ✓ blog/"+post["slug"]+".html")

    print(f"\n  Keyword pages ({len(KEYWORDS)}):")
    for i,kw_data in enumerate(KEYWORDS):
        with open(DIST+"/"+kw_data["slug"]+".html","w",encoding="utf-8") as f:
            f.write(build_keyword_page(kw_data))
        progress(i+1,len(KEYWORDS),kw_data["slug"])
    print()

    support={"sitemap.xml":build_sitemap(),"robots.txt":build_robots(),
              "llms.txt":build_llms(),"_config.yml":"# GitHub Pages\nexclude: [build.py]\n"}
    with open(DIST+"/.nojekyll","w") as f: f.write("")
    with open(DIST+"/.github/workflows/deploy.yml","w") as f: f.write(WORKFLOW)
    print("\n  Support files:")
    for fname,content in support.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(content)
        print(f"    ✓ {fname}")
    print("    ✓ .nojekyll  ✓ .github/workflows/deploy.yml")

    total_sz=sum(os.path.getsize(os.path.join(r,fn)) for r,_,files in os.walk(DIST) for fn in files)
    total_files=sum(len(files) for _,_,files in os.walk(DIST))
    report={"build_date":BUILD_DATE,"domain":SITE_DOMAIN,"keyword_pages":len(KEYWORDS),
             "blog_posts":len(BLOG_POSTS),"total_files":total_files,
             "total_size_mb":round(total_sz/1024/1024,2),"affiliate_url":AFFILIATE_URL}
    with open(DIST+"/build-report.json","w") as f: json.dump(report,f,indent=2)
    print("    ✓ build-report.json")

    print(f"""
{'═'*60}
  ✅  BUILD COMPLETE
{'═'*60}
  Keyword pages:    {len(KEYWORDS):>5}
  Blog posts:       {len(BLOG_POSTS):>5}
  Essential pages:  {len(essential):>5}
  Total files:      {total_files:>5}
  Sitemap URLs:     {len(KEYWORDS)+len(BLOG_POSTS)+10:>5}
  Total size:       {round(total_sz/1024/1024,1):>4.1f} MB
  Output:           ./dist/
{'═'*60}

  Repo: https://github.com/brightlane/pixcuts
  Live: {SITE_DOMAIN}/
""")

if __name__=="__main__":
    main()
