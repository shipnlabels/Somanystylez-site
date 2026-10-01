from partials import *

FILENAME = "index.html"
TITLE = "SoManyStylez Entertainment · DJ, MC & Photo Booths in NJ"
DESC = "DJ Kastro and the SoManyStylez team: wedding and Sweet 16 DJs, MCs, SMS Selfie PhotoBooths and event enhancements across New Jersey, Pennsylvania and Delaware. 5.0 rated. Call (609) 782-0269."

GENRES = [
    ("Mainstream", ["Top 40", "Pop", "Hip Hop", "R&B"]),
    ("Throwbacks", ["00s", "90s", "80s"]),
    ("Classics", ["70s", "60s", "50s"]),
    ("Latin", ["Bachata", "Merengue", "Reggaeton", "Salsa"]),
    ("Dance", ["EDM", "House", "Jersey Club", "Dance"]),
    ("Island", ["Reggae", "Soca", "Dancehall"]),
]

def chips():
    out = []
    for group, items in GENRES:
        out.append(f'<div class="reveal"><p class="eyebrow" style="margin-bottom:10px">{group}</p><div class="chips">' + ''.join(f'<span class="chip">{i}</span>' for i in items) + '</div></div>')
    return ''.join(out)

ENH_PREVIEW = [
    ("assets/img/dancing-on-a-cloud.jpg", "Dancing On A Cloud", "Low-lying fog for a first dance that looks like a fairytale."),
    ("assets/img/glow-totems.jpg", "Glow Totems", "Pillars of light framing the booth, matched to any color."),
    ("assets/img/monogram-gobo.jpg", "Monogram Gobo", "Your names or logo projected onto the floor or wall."),
    ("assets/img/uplighting.jpg", "Enhance Your Elegance", "Uplighting that turns any room into your room."),
    ("assets/img/glow-giveaways.jpg", "Premium Giveaways", "Glow tubes, hats, leis and shades for the whole floor."),
    ("assets/img/selfie-booth.jpg", "SMS Selfie Booths", "Open-air DSLR booths with instant prints and sharing."),
]

def enh_cards():
    return ''.join(f'''<a class="enh reveal" href="enhancements.html" data-delay="{i%3}">
  <img src="{img}" alt="{t}" loading="lazy">
  <div class="enh-body"><h3>{t}</h3><p>{d}</p></div>
</a>''' for i, (img, t, d) in enumerate(ENH_PREVIEW))

BODY = f'''
<section class="hero">
  <div class="hero-media">
    <video autoplay muted loop playsinline poster="assets/video/hero-poster.jpg" aria-hidden="true">
      <source src="assets/video/hero-loop.mp4" type="video/mp4">
    </video>
  </div>
  <div class="hero-veil"></div>
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">So Many Namez, So Many Stylez, We Are So Versatile</span>
      <h1 style="margin-top:16px">Leaving dance floors <span class="grad">smoking</span> since 2014.</h1>
      <p class="lead" style="margin-top:20px">DJ &amp; MC entertainment, SMS Selfie PhotoBooths and full event enhancements for weddings, Sweet 16s, proms and corporate nights across New Jersey, Pennsylvania and Delaware.</p>
      <div class="hero-cta" style="margin-top:28px">
        <a class="btn btn-primary" href="contact.html">Check availability {ICON_ARROW}</a>
        <a class="btn btn-ghost" href="#promo">{ICON_PLAY_GHOST} Watch the promo</a>
      </div>
      <div class="hero-trust">
        <span>{STARS} 5.0 on WeddingWire &amp; The Knot</span>
        <span>15+ years of DJ/MC experience</span>
        <span>Based in Jackson, NJ</span>
      </div>
    </div>
    <div class="hero-side">
      <div class="big">5.0<small>WeddingWire · The Knot</small></div>
    </div>
  </div>
  <div class="scroll-hint" aria-hidden="true"></div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">
  {''.join('<span>Weddings</span><span>Sweet 16s</span><span>Quinceañeras</span><span>Proms</span><span>School Events</span><span>Anniversaries</span><span>Corporate</span><span>Holiday Parties</span><span>Birthdays</span><span>Private Events</span>' for _ in range(2))}
</div></div>

<section class="section" id="promo">
  <div class="wrap">
    <div class="section-head split reveal">
      <div>
        <span class="eyebrow">The SMS experience</span>
        <h2 style="margin-top:12px">Three minutes inside one of our nights.</h2>
      </div>
      <p class="lead">Sound on. This is what a SoManyStylez wedding looks and feels like, from the first dance to the last song.</p>
    </div>
    <div class="feature-video reveal">
      <video preload="metadata" playsinline poster="assets/video/promo-poster.jpg">
        <source src="assets/video/sms-promo-720p.mp4" type="video/mp4">
      </video>
      <img class="poster" src="assets/video/promo-poster.jpg" alt="DJ Kastro on the dance floor at a wedding reception">
      <button class="play" aria-label="Play the SoManyStylez promo video"><span class="play-btn">{ICON_PLAY}</span></button>
    </div>
    <div class="video-caption"><span>SMS Promo · 3:38 · filmed at a real SoManyStylez wedding</span><span>Turn your sound on</span></div>
  </div>
</section>

<section class="section glow-bg" style="padding-top:0">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">What we do</span>
      <h2>One team. The whole night handled.</h2>
      <p class="lead">Book the DJ, add the booth, light the room. Everything comes from one crew that has done this hundreds of times, so nothing falls through the cracks on your day.</p>
    </div>
    <div class="bento">
      <a class="tile b1 reveal" href="weddings.html">
        <img src="assets/img/still-dancefloor.jpg" alt="Guests dancing under purple lighting at a SoManyStylez wedding" loading="lazy">
        <span class="pill solid">Signature service</span>
        <div class="tile-body"><h3>DJ &amp; MC Entertainment</h3><p>Professional DJs and MCs with a decade-plus each behind the decks. Song requests and a do-not-play list are always included.</p><span class="more">Weddings &amp; events {ICON_ARROW}</span></div>
      </a>
      <a class="tile b2 reveal" href="photo-booth.html" data-delay="1">
        <img src="assets/img/selfie-booth.jpg" alt="SMS Selfie open-air photo booth set up at a venue" loading="lazy">
        <div class="tile-body"><h3>SMS Selfie PhotoBooths</h3><p>Open-air DSLR booths. Unlimited prints, instant text and email delivery.</p><span class="more">See the booths {ICON_ARROW}</span></div>
      </a>
      <a class="tile b3 reveal" href="enhancements.html" data-delay="2">
        <img src="assets/img/glow-totems.jpg" alt="Glow totems lining a dance floor" loading="lazy">
        <div class="tile-body"><h3>Event Enhancements</h3><p>Dancing on a cloud, glow totems, uplighting, monogram gobos, cold sparks and more.</p><span class="more">All enhancements {ICON_ARROW}</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap split">
    <div class="split-copy">
      <span class="eyebrow">The music</span>
      <h2>Every era. Every genre. Your crowd.</h2>
      <p class="lead">From the 50s to this week's chart, in English and Spanish. Fill out our song request sheet and your DJ builds the night around your people, then reads the floor and blends it live.</p>
      <div class="eq" aria-hidden="true"></div>
      <p class="muted" style="font-size:.9rem">Song request &amp; do-not-play list included with every booking.</p>
    </div>
    <div style="display:grid;gap:22px">{chips()}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Why SoManyStylez</span>
      <h2>Professional. Affordable. There when we say we'll be.</h2>
    </div>
    <div class="pillars">
      <div class="pillar reveal"><span class="n">01</span><h3>Professionalism</h3><p>Your wedding or special event runs smoothly from beginning to end. Every SMS DJ has over a decade of professional DJ and MC experience.</p></div>
      <div class="pillar reveal" data-delay="1"><span class="n">02</span><h3>Affordability</h3><p>An unforgettable night within your budget. You deserve an affordable DJ without jeopardizing the success of your event.</p></div>
      <div class="pillar reveal" data-delay="2"><span class="n">03</span><h3>Reliability</h3><p>You'll never have to worry about your DJ not showing up on your big day. Our DJs are trustworthy, prepared and ready to serve you.</p></div>
    </div>
    <p class="pull reveal" style="margin-top:clamp(40px,6vw,72px)">You don't always get what you pay for. <em>Sometimes you get more.</em></p>
  </div>
</section>

<section class="section glow-bg" style="padding-top:0">
  <div class="wrap">
    <div class="section-head split reveal">
      <div><span class="eyebrow">Event enhancements</span><h2 style="margin-top:12px">Turn a party into a production.</h2></div>
      <a class="btn btn-ghost" href="enhancements.html">All enhancements {ICON_ARROW}</a>
    </div>
    <div class="snap">{enh_cards()}</div>
  </div>
</section>

<section class="section band">
  <div class="wrap split rev">
    <div class="split-media tall"><img src="assets/img/dj-kastro-turntables.jpg" alt="DJ Kastro on the turntables" loading="lazy"></div>
    <div class="split-copy">
      <span class="eyebrow">Meet the owner</span>
      <h2>DJ Kastro. The Cuban Turntable Assassin.</h2>
      <p class="lead">Robert Douriet started with house parties in Lakewood, held down a bar residency, produced Jersey Club records, then built SoManyStylez in 2014 around one promise: a quality atmosphere and real professionalism for any occasion.</p>
      <ul>
        <li class="check">Founder, owner and lead DJ/MC</li>
        <li class="check">Hip Hop, R&amp;B, House, Dance, Reggae and Reggaeton roots</li>
        <li class="check">Hundreds of weddings, Sweet 16s, proms and corporate events</li>
      </ul>
      <div><a class="btn btn-ghost" href="about.html">His story {ICON_ARROW}</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="stats reveal">
      <div class="stat"><b class="grad">5.0</b><span>Average rating on WeddingWire and The Knot</span></div>
      <div class="stat"><b>15<span style="font-size:.6em">+</span></b><span>Years of professional DJ/MC experience</span></div>
      <div class="stat"><b>2014</b><span>SoManyStylez Entertainment founded</span></div>
      <div class="stat"><b>3</b><span>States served: New Jersey, Pennsylvania, Delaware</span></div>
    </div>
    <div class="grid-2" style="margin-top:18px">
      <figure class="card reveal" style="margin:0"><div class="card-body" style="padding:28px;gap:14px">
        {STARS}
        <blockquote style="margin:0;font-family:var(--display);font-size:1.35rem;font-weight:600;line-height:1.3;letter-spacing:-.01em">"Fantastic music and an incredible photo booth. A local business owner who continues to go above and beyond for the clients."</blockquote>
        <figcaption class="muted" style="font-size:.9rem">Jersey Shore Online, covering the Jackson Township prom</figcaption>
      </div></figure>
      <div class="card reveal" data-delay="1"><div class="card-body" style="padding:28px;gap:14px">
        <span class="eyebrow">Trusted on</span>
        <div style="display:flex;flex-wrap:wrap;gap:10px"><span class="chip"><strong>WeddingWire</strong>&nbsp;5.0</span><span class="chip"><strong>The Knot</strong>&nbsp;5.0</span><span class="chip"><strong>Facebook</strong>&nbsp;Recommended</span></div>
        <p style="color:var(--fg-2)">Read what couples and parents say, then check our date availability. Most dates in peak season fill months ahead.</p>
        <div><a class="btn btn-primary btn-sm" href="contact.html">Check my date {ICON_ARROW}</a></div>
      </div></div>
    </div>
  </div>
</section>

{cta_band()}
'''
