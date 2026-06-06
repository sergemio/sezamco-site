---
name: on-page-seo-best-practices
description: The comprehensive on-page SEO checklist (15 categories, 88 items) — read before generating any new page (blog post or service page) for Sezam&Co or any project
metadata:
  type: reference
---

# On-page SEO — do these on every page

> **THE COMPREHENSIVE ON-PAGE SEO CHECKLIST**
> 15 categories · 88 items · the complete on-page SEO spec for blog posts and service pages. Technical SEO (sitemaps, robots.txt, Core Web Vitals) is covered separately.
>
> **Save this as `on-page-seo-best-practices.md`** — every page-generation skill reads it before generating any page.

---

## 1. HEAD & METADATA — What Google indexes first
- [ ] **Title tag** — 50–60 chars, primary keyword near the start.
- [ ] **Meta description** — 150–160 chars, keyword + benefit + soft CTA.
- [ ] **Canonical URL** set to prevent duplicates.
- [ ] **Open Graph** — `og:title`, `og:description`, `og:image` (1200×630), `og:url`, `og:type`.
- [ ] **Twitter Card** — `summary_large_image`, title, description, image.
- [ ] **Language** attribute on `<html>` (e.g. `lang="en"`).
- [ ] **Viewport meta** tag for responsive rendering.
- [ ] **Favicon** + `apple-touch-icon`.
- [ ] **Charset meta** — `<meta charset="utf-8">`.

## 2. URL STRUCTURE — Clean, readable, keyword-forward
- [ ] **Short slug** — under 60 chars.
- [ ] **Primary keyword** in the slug.
- [ ] **Hyphens** only — never underscores.
- [ ] **Lowercase** only.
- [ ] **No stop words** ("the", "a", "of") unless necessary.
- [ ] **Logical hierarchy** — `/services/[slug]`, `/blog/[slug]`.

## 3. HEADINGS — Structure for skimmers & bots
- [ ] **Exactly one H1** per page, contains primary keyword.
- [ ] **Logical H2 → H3** hierarchy — never skip levels.
- [ ] **H2s** use supporting keywords + questions from the cluster.
- [ ] **No keyword stuffing** — write naturally.

## 4. COPY & BODY — Answer the query, fast
- [ ] **Primary keyword** in the first 100 words.
- [ ] **Direct answer** to the query in the first paragraph.
- [ ] **Length** matches SERP average (within 20% of top-3).
- [ ] **Short paragraphs** (1–4 sentences).
- [ ] **Readability** — 8th–10th grade level.
- [ ] **Active voice** preferred.
- [ ] **Bold key phrases** — sparingly.
- [ ] **Bullets & numbered lists** where appropriate.

## 5. FAQ SECTION — Every blog post
- [ ] **4–8 questions** from SEMRush Questions tab + "People Also Ask".
- [ ] **Direct answers** — 2–4 sentences each.
- [ ] **FAQ schema** (JSON-LD) applied.

## 6. IMAGES — Every image is a ranking signal
- [ ] **Alt text** describes image + keyword where natural.
- [ ] **Filenames** — descriptive, hyphens, e.g. `emergency-plumber-toronto.webp`.
- [ ] **WebP**, compressed under 200 KB.
- [ ] **Width/height** attributes specified — prevents CLS.
- [ ] **Lazy loading** (`loading="lazy"`) for below-fold.
- [ ] **Responsive srcset** where needed.
- [ ] **Featured/hero image** for social sharing.

## 7. INTERNAL LINKS — Pass authority across the site
- [ ] **3–5 internal links** per post.
- [ ] Link to **related blog posts & relevant service pages**.
- [ ] **Descriptive anchor text** — never "click here" or "read more".
- [ ] **Contextually placed** in body copy.
- [ ] **Breadcrumbs** on every page.

## 8. EXTERNAL LINKS — Cite authority, don't hoard it
- [ ] **2–3 external links** to authoritative sources (.gov, .edu, major industry).
- [ ] **Relevant** to the topic.
- [ ] Open in **new tab** with `rel="noopener"`.
- [ ] `rel="nofollow"` for sponsored links.

## 9. SCHEMA MARKUP — JSON-LD in `<head>`
- [ ] **Article** schema on blog posts.
- [ ] **LocalBusiness** schema — most specific subtype (Plumber, Dentist...).
- [ ] **Service** schema on service pages.
- [ ] **FAQ** schema wherever FAQ section exists.
- [ ] **BreadcrumbList** schema on every page.
- [ ] **Organization** schema site-wide.
- [ ] **Author/Person** schema for bylines.

## 10. E-E-A-T SIGNALS — Experience · Expertise · Authority · Trust
- [ ] **Author byline** with name on every blog post.
- [ ] **Author bio** with credentials (years, qualifications).
- [ ] Link to **author's dedicated page**.
- [ ] **Published date** displayed.
- [ ] **"Last updated"** date when refreshed.
- [ ] **Real stories, numbers, opinions** from the business voice file.
- [ ] **Cite authoritative sources**.
- [ ] **About page** with full company credentials.
- [ ] **Contact page** — real address, phone, hours.

## 11. ACCESSIBILITY — A11y signals = SEO signals
- [ ] **Semantic HTML5** — `<header>`, `<nav>`, `<main>`, `<article>`, `<footer>`.
- [ ] **ARIA labels** on interactive elements where needed.
- [ ] **Color contrast** meets WCAG AA (4.5:1 body text).
- [ ] **Focus indicators** visible on interactive elements.
- [ ] **Alt text** on all images (empty `alt=""` for decorative).
- [ ] **Descriptive link text**.
- [ ] **Skip-to-content** link for keyboard users.

## 12. MOBILE & RESPONSIVE — Mobile-first indexing
- [ ] **Responsive layout** (Tailwind handles this).
- [ ] **Touch targets** minimum 48×48 px.
- [ ] **Body font** minimum 16 px.
- [ ] **No horizontal scroll** at any viewport.
- [ ] **No intrusive interstitials**.

## 13. SOCIAL PREVIEW — Shareable card
- [ ] **OG image** optimized — 1200×630, under 1 MB.
- [ ] **Twitter Card image** — 1200×600.
- [ ] **Compelling** `og:description` — different from meta if valuable.

## 14. CONVERSION ELEMENTS — Capture the lead *(SERVICE PAGES ONLY)*
- [ ] **Primary CTA** above the fold.
- [ ] **Phone number** with click-to-call (`tel:`).
- [ ] **Multiple CTA placements** throughout the page.
- [ ] **Trust signals** — reviews, ratings, licenses, years.
- [ ] **Testimonials** with names (photos where possible).
- [ ] **Service-area coverage** listed.
- [ ] **Business hours** displayed.
- [ ] **Physical address** with embedded map.

## 15. LONG-FORM CONTENT — 1500+ word posts
- [ ] **Table of contents** with anchor links at the top.
- [ ] **Jump links** for each H2.
- [ ] **Back-to-top** button.

---

## 📝 Notes & 2026 updates (post-checklist verification)

These notes capture nuances that emerged from cross-checking the checklist against current authoritative sources (May 2026). The checklist items above are kept verbatim from the original source; the notes below add context for items where the spec has evolved or where the original value is more conservative/aggressive than the current standard.

### Card 5 & Card 9 — FAQ schema
**Important 2026 update**: Google **deprecated FAQ rich results in Search on May 7, 2026**. The `FAQPage` schema type is **still valid** and Google still uses it to understand pages (and AI search engines / LLMs leverage it), but it no longer produces a rich result in SERPs. Keep the schema for comprehension/AI search value, but don't expect rich-result SERP bonuses.
*Source: [Google Search Central — FAQPage docs](https://developers.google.com/search/docs/appearance/structured-data/faqpage), [Search Engine Land](https://searchengineland.com/google-to-no-longer-support-faq-rich-results-476957)*

### Card 8 — `rel="nofollow"` for sponsored links
Since 2019, Google recommends **`rel="sponsored"`** (more specific) for paid/sponsored links. `rel="nofollow"` still works as a generic signal, but the modern convention is:
- `rel="sponsored"` → paid/affiliate links
- `rel="ugc"` → user-generated content (forums, comments)
- `rel="nofollow"` → generic "don't pass authority"

### Card 12 — Touch targets 48×48 px
The official **WCAG 2.2 SC 2.5.8 (Level AA) minimum is 24×24 CSS pixels**. The checklist's 48×48 value corresponds to **Google Material Design** recommendation (Apple HIG = 44×44). The checklist value is more conservative than the strict WCAG minimum — better for UX, just not the lowest legal bar.
*Source: [W3C WCAG 2.2 Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)*

### Card 13 — Twitter Card image 1200×600
**Likely typo in source**. Official Twitter/X `summary_large_image` specs in 2026 are:
- **1200×675** (16:9 ratio, pure Twitter spec), OR
- **1200×628** (1.91:1, cross-platform compatible with Facebook/LinkedIn — allows reusing the same image as `og:image`)

**Recommendation**: use **1200×628** or **1200×675**, not 1200×600.
*Source: [X Developer Platform — Summary Card with Large Image](https://developer.x.com/en/docs/x-for-websites/cards/overview/summary-card-with-large-image)*

### Card 15 — "1500+ word posts"
Word count is **not** a Google ranking signal (confirmed multiple times by John Mueller). The 1500-word threshold is a **community heuristic** based on observed averages of top-10 SERP results for competitive informational queries. Use as a depth proxy, not a target.
*Source: [Yoast — Word count and SEO](https://yoast.com/blog-post-word-count-seo/)*

### Card 4 — "Length matches SERP average (within 20% of top-3)"
This is a SurferSEO/Clearscope/PageOptimizer Pro heuristic, not a Google official rule. Useful guideline, but write for completeness first, target length second.

### Bonus — Items the checklist does NOT cover (but worth knowing)
The checklist explicitly excludes Technical SEO (sitemaps, robots.txt, Core Web Vitals) — covered separately. Other items occasionally worth considering:
- `theme-color` meta tag (PWA / browser chrome color)
- `manifest.json` for PWA installability
- `hreflang` for multi-language sites
- IndexNow protocol for instant indexing (Bing + Yandex)
- AI/LLM-specific schema like `Person.knowsAbout`, `Article.about`/`mentions` for AI search visibility

These are out of scope of this specific checklist but worth keeping in mind for Sezam&Co or any project.

---

## 🌐 Sources (cross-check May 2026)

- [Twitter / X Card Image Size — 1200×675px (2026 Guide) | Moda](https://moda.app/resources/sizes/twitter-card)
- [Summary Card with Large Image — X Developer Platform](https://developer.x.com/en/docs/x-for-websites/cards/overview/summary-card-with-large-image)
- [Facebook OG Image Size & Requirements 2026 | OGrilla](https://www.ogrilla.com/blog/facebook-og-image-size)
- [Open Graph Image Sizes 2026 Complete Guide | Krumzi](https://www.krumzi.com/blog/open-graph-image-sizes-for-social-media-the-complete-2026-guide)
- [Understanding Success Criterion 2.5.8: Target Size (Minimum) | W3C](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [Meta Title Length Best Practices 2026 | Scalenut](https://www.scalenut.com/blogs/meta-title-length-best-practices-2026)
- [The Best Title Tag Length for Google SEO | Zyppy](https://zyppy.com/title-tags/meta-title-tag-length/)
- [Meta Description Length 2026 SEO Best Practices | Letter Counter](https://lettercounter.org/blog/meta-description-length-seo-guide/)
- [rel="noopener" HTML attribute value — MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener)
- [Links to cross-origin destinations are unsafe — Lighthouse | Chrome](https://developer.chrome.com/docs/lighthouse/best-practices/external-anchors-use-rel-noopener)
- [Google FAQ Rich Results Are No Longer Supported — May 2026 | ALM Corp](https://almcorp.com/blog/google-faq-rich-results-no-longer-supported/)
- [Google to no longer support FAQ rich results | Search Engine Land](https://searchengineland.com/google-to-no-longer-support-faq-rich-results-476957)
- [Mark Up FAQs with Structured Data | Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/faqpage)
- [SEO Word Count in 2026 — Blog Post Length to Rank on Google](https://wordscountertool.com/seo-word-count-in-2026-blog-post-length-to-rank-on-google/)
- [Word count and SEO — Yoast](https://yoast.com/blog-post-word-count-seo/)
- [16px or Larger Text Prevents iOS Form Zoom | CSS-Tricks](https://css-tricks.com/16px-or-larger-text-prevents-ios-form-zoom/)
- [Image Optimization for The Web: 2026 Proven Techniques | Nitropack](https://nitropack.io/blog/image-optimization-for-the-web-the-essential-guide/)
- [WebP/AVIF Image Compression for SEO 2026 | Cloud SEO](https://seoservices.cloud/en/blog/nen-anh-webp-avif-chuan-seo-2026/)

---

*Last verified: 2026-05-17*
