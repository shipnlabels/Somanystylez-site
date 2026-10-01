# SoManyStylez Entertainment — new website

Static, multi-page site. No framework, no build step required to host it: upload the
folder to any host (GoDaddy, Netlify, Cloudflare Pages, Vercel, plain cPanel).

Live preview (private): https://claude.ai/artifact/83cd4UCzT83yYTZ29Ldovw

## Pages
| File | Page |
|---|---|
| index.html | Home: hero video loop, full promo with sound, services, music, why us, enhancements, DJ Kastro, ratings |
| weddings.html | Ceremony / cocktail / reception flow, Bronze–Diamond tiers, signature moments, FAQ |
| events.html | Sweet 16 & Quinceañera packages with prices, proms, anniversaries, corporate |
| photo-booth.html | SMS Selfie PhotoBooths: inclusions, 4 booth models, LED add-ons, how it works, FAQ |
| enhancements.html | All 15 enhancements with photos, popular combinations |
| gallery.html | Full promo video (sound on) + photo grid |
| about.html | DJ Kastro bio, timeline, mission, pillars, team |
| faq.html | DJ and photo booth questions |
| contact.html | Phone, email, socials, booking form, what happens next |

## Folder
- `css/styles.css` — all styling (design tokens at the top)
- `js/main.js` — menu, scroll reveals, video player, copy buttons, booking form
- `assets/img/` — logo variants (`logo-white.png`, `logo-dark.png`, `mark.png`, `wordmark-*.png`, `logo-original.png`) and every photo
- `assets/video/` — `hero-loop.mp4` (31 s, muted, 4.5 MB), `sms-promo-720p.mp4` (full promo with sound, 52 MB),
  `sms-promo-480p.mp4` (12 MB copy used on the preview link), posters
- `build/` — Python generator that produces the pages from shared header/footer partials.
  Edit `build/page_*.py` or `build/partials.py`, then run `python3 build/build.py`. Hosting does not need this folder.

## Before going live
1. **Booking form.** "Send availability request" opens the visitor's mail app with a prefilled email to the business
   address (subject, every field, add-ons and notes), and shows Text / Copy fallbacks. No backend needed. If you'd rather
   receive submissions without relying on the visitor's mail app, point the form at Formspree or Netlify Forms.
2. **Confirm the email.** The site uses `SoManyStylezEnt@gmail.com` (from public listings). A Facebook listing also shows
   `Somanystylezent16@gmail.com`. Set the right one in `build/partials.py` (`EMAIL`) and rebuild.
3. **Reviews.** Only verifiable facts are on the site (5.0 on WeddingWire and The Knot, the Jersey Shore Online quote).
   Add real client quotes to the Home and Weddings pages once the client supplies them.
4. **Pricing.** Sweet 16 prices and photo booth add-ons are copied from the current site. Wedding tiers are "Contact for pricing"
   as on his price list. Confirm all numbers are current.
5. **Full video on hosting.** Use `sms-promo-720p.mp4` on the real host (the preview link uses the 480p copy because of a per-file size limit).
   The hero loop is muted by design: browsers block autoplay with sound.
6. **Analytics / pixel.** Add the Facebook pixel and Google Analytics tags in `build/partials.py` → `head()` and rebuild.
7. **Domain.** Point somanystylezentertainment.com at the new host; keep the same page names if you want to keep any old links alive
   (the old GoDaddy URLs like `/weddings-1` and `/sms-selfie-photobooths` can be redirected to `weddings.html` and `photo-booth.html`).

## Social accounts
- Facebook: facebook.com/SoManyStylezEnt · Instagram: @therealdjkastro (his price list also shows @SoManyStylez_Entertainment) ·
  TikTok: @therealdjkastro · YouTube: @SoManyStylezEntertainment (the old site linked a YouTube handle that no longer exists; fixed here).
- Facebook, Instagram and TikTok don't expose photos without a login, so the gallery uses only what was on his site and in his promo.
  Ask him for a folder of event photos to grow the Gallery; drop them in `assets/img/` and add a line in `build/page_gallery.py`.

## Two images to know about
- `assets/img/cold-sparks.jpg` is his first-dance still with a rendered spark-fountain effect, because he has no photo of
  his cold sparks yet. Swap in a real photo with the same filename when he has one.
- `assets/img/snapchat-geofilter.jpg` is his actual Monroe Township prom geofilter composited over one of his prom photos.

## What came from the old site
Logo, tagline, phone, services, genres, the three pillars, FAQ answers, Sweet 16 packages and prices, wedding tier contents,
photo booth features and FAQ, DJ Kastro's bio, the Event Enhancements list with its photos, the gallery DJ photos, and the promo video.
Empty template pages and the stray YouTube embeds were dropped.
