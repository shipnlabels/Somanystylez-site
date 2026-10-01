from partials import *

FILENAME = "gallery.html"
TITLE = "Gallery · SoManyStylez Entertainment"
DESC = "Photos and the full promo video from SoManyStylez Entertainment: weddings, Sweet 16s, proms, photo booths and event lighting across New Jersey."

PHOTOS = [
    ("assets/img/still-first-dance.jpg", "Grand entrance through the fog"),
    ("assets/img/still-couple-dance.jpg", "First dance"),
    ("assets/img/dj-kastro-decks.jpg", "DJ Kastro on the decks"),
    ("assets/img/dancing-on-a-cloud.jpg", "Dancing on a cloud"),
    ("assets/img/glow-totems.jpg", "Glow totems lining the floor"),
    ("assets/img/still-dancefloor.jpg", "Packed dance floor"),
    ("assets/img/monogram-gobo.jpg", "Custom monogram gobo for a Sweet 16"),
    ("assets/img/dj-kastro-mic.jpg", "On the mic"),
    ("assets/img/uplighting.jpg", "Uplighting in the dining room"),
    ("assets/img/still-booth-guests.jpg", "Guests in the photo booth"),
    ("assets/img/prom-crowd.jpg", "Prom night"),
    ("assets/img/prom-dance.jpg", "Prom dance floor"),
    ("assets/img/selfie-booth.jpg", "SMS Selfie Booth setup"),
    ("assets/img/ceremony.jpg", "Ceremony moment"),
    ("assets/img/still-cake.jpg", "Cake table"),
    ("assets/img/dj-setup-totems.jpg", "Booth with screens and totems"),
    ("assets/img/dj-kastro-booth.jpg", "Late night at the booth"),
    ("assets/img/glow-giveaways.jpg", "Premium glow giveaways"),
    ("assets/img/audio-guestbook.jpg", "Audio guestbook"),
    ("assets/img/dj-kastro-turntables.jpg", "Turntables"),
]

def masonry():
    return ''.join(f'<figure class="reveal" data-delay="{i%3}"><img src="{s}" alt="{a}" loading="lazy"><figcaption>{a}</figcaption></figure>' for i, (s, a) in enumerate(PHOTOS))

BODY = f'''
<section class="page-hero" style="min-height:auto;padding-bottom:24px">
  <div class="hero-media"><img src="assets/img/still-dancefloor.jpg" alt="" fetchpriority="high" style="opacity:.5"></div>
  <div class="hero-veil"></div>
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a><span>/</span><span>Gallery</span></div>
    <span class="eyebrow">Gallery</span>
    <h1 style="margin-top:14px">See it. <span class="grad">Hear it.</span></h1>
    <p class="lead" style="margin-top:18px">The full SMS promo with sound, then the photos. Everything here is from real SoManyStylez events.</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap">
    <div class="feature-video reveal">
      <video preload="metadata" playsinline poster="assets/video/promo-poster.jpg">
        <source src="assets/video/sms-promo-720p.mp4" type="video/mp4">
      </video>
      <img class="poster" src="assets/video/promo-poster.jpg" alt="SoManyStylez promo video poster">
      <button class="play" aria-label="Play the SoManyStylez promo video"><span class="play-btn">{ICON_PLAY}</span></button>
    </div>
    <div class="video-caption"><span>SMS Promo · 3:38 · sound on</span><a href="https://vimeo.com/1031784364" target="_blank" rel="noopener">Also on Vimeo</a></div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap">
    <div class="section-head reveal" style="margin-bottom:18px"><span class="eyebrow">More videos</span><h2>Booth demos and highlight reels.</h2></div>
    <div class="grid-4">{yt_cards()}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Photos</span><h2>Nights we were part of.</h2></div>
    <div class="masonry">{masonry()}</div>
    <p class="muted reveal" style="margin-top:22px;font-size:.9rem">Want to see more? Follow <a href="https://www.instagram.com/therealdjkastro" target="_blank" rel="noopener" style="text-decoration:underline">@therealdjkastro</a> on Instagram for the latest events.</p>
  </div>
</section>

{cta_band("Want this at your event?", "Tell us the date and we'll check availability within 24 to 72 hours.")}
'''
