from partials import *

FILENAME = "events.html"
TITLE = "Sweet 16, Prom & Corporate DJs · SoManyStylez Entertainment"
DESC = "Sweet 16 and Quinceañera packages from $850, proms and school events, anniversaries, holiday parties and corporate events. SoManyStylez Entertainment, Jackson NJ."

PK = [
    ("Basic", "850", "1,400", ["4 to 5 hours of entertainment", "1 DJ/Emcee entertainer", "Basic sound system", "Basic dance floor lighting"], False),
    ("Supreme", "1,250", "1,700", ["4 to 5 hours of entertainment", "1 DJ/Emcee entertainer + 1 Emcee", "Standard sound system", "Supreme dance floor lighting with LED table-top façade", "Uplighting", "Monogram"], False),
    ("Platinum", "1,650", "2,100", ["4 to 5 hours of entertainment", "Professional sound system", "Platinum dance floor lighting with LED full-panel façade", "Intelligent lighting", "Custom monogram gobo", "Giveaways: glow sticks, hats, leis and sunglasses", "Audio guestbook"], True),
    ("Diamond", "2,250", "2,850", ["Everything in Platinum", "Premium giveaways: glow batons, hats, leis and sunglasses", "Dancing on clouds"], False),
    ("Prince / Princess", "2,800", "3,450", ["Everything in Diamond", "Cold sparks", "Glow totems", "SMS Visualz (booth only)"], False),
    ("Fairytale", "3,500", "4,050", ["Everything in Prince / Princess", "SMS Visualz (complete)"], False),
]

def packages():
    out = []
    for i, (n, p, pb, items, hot) in enumerate(PK):
        out.append(f'''<div class="pkg{' hot' if hot else ''} reveal" data-delay="{i%3}">
  <h3>{n}</h3>
  <div class="price"><b class="tabular">${p}</b><span>DJ package</span></div>
  <div class="with">With SMS Selfie PhotoBooth: <strong class="tabular">${pb}</strong></div>
  <ul>{''.join(f'<li>{x}</li>' for x in items)}</ul>
  <a class="btn btn-ghost btn-sm" href="contact.html">Book {n} {ICON_ARROW}</a>
</div>''')
    return ''.join(out)

BODY = page_hero(
    "Events",
    "Sweet 16s, proms and every <span class=\"grad\">big night</span> between.",
    "Birthdays, Quinceañeras, school events, anniversaries, holiday parties and corporate functions. If there's a dance floor, we know how to fill it.",
    "assets/img/prom-crowd.jpg",
    crumbs="<span>Events</span>") + f'''

<section class="section-tight">
  <div class="wrap">
    <div class="chips reveal">
      <a class="chip" href="#sweet16">Sweet 16 &amp; Quinceañera</a>
      <a class="chip" href="#prom">Proms &amp; School Events</a>
      <a class="chip" href="#anniversary">Anniversaries &amp; Birthdays</a>
      <a class="chip" href="#corporate">Corporate &amp; Holiday</a>
    </div>
  </div>
</section>

<section class="section band" id="sweet16" style="scroll-margin-top:90px">
  <div class="wrap">
    <div class="section-head split reveal">
      <div><span class="eyebrow">Sweet 16 &amp; Quinceañera</span><h2 style="margin-top:12px">Packages built for the biggest birthday yet.</h2></div>
      <p class="lead">Clear pricing, every tier includes the one before it, and the SMS Selfie PhotoBooth can be bundled into any of them.</p>
    </div>
    <div class="packages">{packages()}</div>
    <p class="muted reveal" style="margin-top:18px;font-size:.9rem">Travel outside central New Jersey, extra hours and additional DJs or MCs are quoted separately. A deposit holds your date.</p>
  </div>
</section>

<section class="section" id="prom" style="scroll-margin-top:90px">
  <div class="wrap split">
    <div class="split-media"><img src="assets/img/prom-dance.jpg" alt="Prom dance floor" loading="lazy"></div>
    <div class="split-copy">
      <span class="eyebrow">Proms &amp; school events</span>
      <h2>Clean edits. Big energy. Chaperone approved.</h2>
      <p class="lead">Radio-clean music, an MC who can run a grand march or a crowning, and a crew that shows up early and sets up quietly. We've been the team behind Jackson Township's prom night more than once.</p>
      <ul>
        <li class="check">Clean versions of everything, no exceptions</li>
        <li class="check">Game and dance motivator keeps the floor moving</li>
        <li class="check">Add the photo booth, glow totems or premium giveaways</li>
      </ul>
      <figure class="card" style="margin:0;padding:20px;display:grid;gap:8px">
        {STARS}
        <blockquote style="margin:0;font-weight:600">"Fantastic music and an incredible photo booth."</blockquote>
        <figcaption class="muted" style="font-size:.86rem">Jersey Shore Online, on the Jackson Township prom</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section band" id="anniversary" style="scroll-margin-top:90px">
  <div class="wrap split rev">
    <div class="split-media"><img src="assets/img/uplighting.jpg" alt="Banquet tables washed in purple uplighting" loading="lazy"></div>
    <div class="split-copy">
      <span class="eyebrow">Anniversaries &amp; birthdays</span>
      <h2>Their decade. Their songs.</h2>
      <p class="lead">A 50th anniversary needs a different DJ than a 30th birthday. Our collection runs from the 50s to this week, and we take the time to learn the songs that mean something to the guest of honor.</p>
      <ul>
        <li class="check">Song request sheet so family can add the classics</li>
        <li class="check">Volume that lets people talk, then rises for the dance set</li>
        <li class="check">Uplighting and a monogram to make the room theirs</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="corporate" style="scroll-margin-top:90px">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Corporate &amp; holiday parties</span><h2>Professional on the mic. Fun on the floor.</h2></div>
    <div class="grid-3">
      <div class="card reveal"><div class="card-media"><img src="assets/img/dj-setup-totems.jpg" alt="DJ booth with branded screens and totems" loading="lazy"></div><div class="card-body"><h3>Branded visuals</h3><p>SMS Visualz puts your logo, slideshow or social feed on screens at the booth.</p></div></div>
      <div class="card reveal" data-delay="1"><div class="card-media"><img src="assets/img/selfie-booth.jpg" alt="Open-air selfie booth" loading="lazy"></div><div class="card-body"><h3>Photo booth with your logo</h3><p>Custom templates on every print and every share. Great for holiday parties and launches.</p></div></div>
      <div class="card reveal" data-delay="2"><div class="card-media"><img src="assets/img/dj-kastro-mic.jpg" alt="DJ Kastro on the microphone" loading="lazy"></div><div class="card-body"><h3>An MC who runs the room</h3><p>Awards, raffles, announcements and a timeline kept on schedule.</p></div></div>
    </div>
  </div>
</section>

{cta_band("Tell us about the event.", "Date, venue, headcount and the vibe you want. We'll come back with availability and a quote within 24 to 72 hours.")}
'''
