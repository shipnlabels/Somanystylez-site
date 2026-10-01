from partials import *

FILENAME = "weddings.html"
TITLE = "Wedding DJs & MCs · SoManyStylez Entertainment"
DESC = "Wedding DJ and MC packages from SoManyStylez Entertainment in Jackson, NJ. Ceremony, cocktail hour and reception, with dancing on a cloud, monogram gobos, uplighting, photo booths and cold sparks."

TIERS = [
    ("Bronze", "Up to 70 guests", ["1 DJ/MC, 4-hour reception", "Basic sound system", "Basic lighting"], []),
    ("Silver", "Up to 120 guests", ["1 DJ/MC", "Standard sound system", "Basic lighting"], ["Ceremony", "Cocktail hour"]),
    ("Gold", "Up to 150 guests", ["2 DJs / 1 MC", "Standard sound system", "Intelligent lighting with glow totems", "Monogram gobo"], ["Ceremony", "Cocktail hour", "Uplighting"]),
    ("Platinum", "Up to 150 guests", ["2 DJs / 1 MC", "Pro sound system", "Intelligent lighting with glow totems", "Monogram gobo", "SMS Selfie PhotoBooth"], ["Ceremony", "Cocktail hour", "Uplighting"]),
    ("Diamond", "150 guests and up", ["2 DJs / 1 MC", "Pro sound system", "Intelligent lighting with glow totems", "Monogram gobo", "SMS Selfie PhotoBooth"], ["Ceremony", "Cocktail hour", "Uplighting", "Dancing on a cloud", "SMS Visualz", "Cold sparks"]),
]

def tiers():
    out = []
    for i, (name, cap, inc, plus) in enumerate(TIERS):
        hot = ' hot' if name == "Platinum" else ''
        items = ''.join(f'<li>{x}</li>' for x in inc) + ''.join(f'<li class="plus">{x}</li>' for x in plus)
        out.append(f'''<div class="pkg{hot} reveal" data-delay="{i%3}">
  <div><span class="eyebrow">{cap}</span><h3 style="margin-top:8px">{name}</h3></div>
  <div class="price"><b>Contact</b><span>for pricing</span></div>
  <ul>{items}</ul>
  <a class="btn btn-ghost btn-sm" href="contact.html">Ask about {name} {ICON_ARROW}</a>
</div>''')
    return ''.join(out)

BODY = page_hero(
    "Weddings",
    "First dance to <span class=\"grad\">forever.</span>",
    "Let us create a moment that will last forever. One crew handles your ceremony, cocktail hour and reception, so the music, the mic and the lights all move together.",
    "assets/img/still-first-dance.jpg",
    crumbs="<span>Weddings</span>") + f'''

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">How your day flows</span>
      <h2>Three moments. One seamless night.</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><span class="k">CEREMONY</span><h3>Walk in to your song.</h3><p>Discreet sound for the processional, your officiant mic'd and clear, and the recessional hitting exactly on your kiss.</p></div>
      <div class="step reveal" data-delay="1"><span class="k">COCKTAIL HOUR</span><h3>Set the mood.</h3><p>A separate sound setup so guests can hear each other over a curated mix while the room fills up.</p></div>
      <div class="step reveal" data-delay="2"><span class="k">RECEPTION</span><h3>Pack the floor.</h3><p>Introductions, first dance, toasts and then four hours of non-stop music. Our DJs don't take breaks unless you ask them to.</p></div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head split reveal">
      <div><span class="eyebrow">Wedding packages</span><h2 style="margin-top:12px">Pick a tier. Add what you love.</h2></div>
      <p class="lead">Every tier includes what the one before it has. Pricing depends on date, venue and hours, so tell us about your day and we'll send a quote.</p>
    </div>
    <div class="packages five">{tiers()}</div>
    <p class="muted reveal" style="margin-top:18px;font-size:.9rem">Need something between tiers? Any enhancement can be added to any package.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-media"><img src="assets/img/dancing-on-a-cloud.jpg" alt="A couple's first dance on a cloud of low-lying fog" loading="lazy"></div>
    <div class="split-copy">
      <span class="eyebrow">Signature wedding moments</span>
      <h2>The first dance, on a cloud.</h2>
      <p class="lead">Low-lying fog that rolls across the floor and stays at your feet. Your photographer will thank you.</p>
      <ul>
        <li class="check"><span><strong>Monogram gobo.</strong> Your names projected onto the floor or wall.</span></li>
        <li class="check"><span><strong>Uplighting.</strong> Wash the room in your wedding colors.</span></li>
        <li class="check"><span><strong>Cold sparks.</strong> Indoor-safe spark fountains for the big entrance or the last dance.</span></li>
        <li class="check"><span><strong>SMS Selfie PhotoBooth.</strong> Unlimited prints, templates matched to your invitations.</span></li>
      </ul>
      <div><a class="btn btn-ghost" href="enhancements.html">See every enhancement {ICON_ARROW}</a></div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">From the promo</span><h2>What a SoManyStylez wedding looks like.</h2></div>
    <div class="grid-3">
      <figure class="card reveal" style="margin:0"><div class="card-media"><img src="assets/img/still-cake.jpg" alt="Wedding cake lit in soft purple" loading="lazy"></div></figure>
      <figure class="card reveal" data-delay="1" style="margin:0"><div class="card-media"><img src="assets/img/still-dancefloor.jpg" alt="Guests dancing at a reception" loading="lazy"></div></figure>
      <figure class="card reveal" data-delay="2" style="margin:0"><div class="card-media"><img src="assets/img/still-booth-guests.jpg" alt="Guests posing in the photo booth" loading="lazy"></div></figure>
    </div>
    <div style="margin-top:22px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary" href="gallery.html">{ICON_PLAY_GHOST} Watch the full promo</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Couples ask</span><h2>Good questions.</h2></div>
    <div class="faq">
      <details><summary>Do you take breaks?</summary><div class="a">No. Our DJ staff performs continuously from the scheduled start time until your party is over, unless you request a break for some other reason.</div></details>
      <details><summary>Can we choose the music?</summary><div class="a">Yes. Fill out our online request sheet and your DJ customizes the night around it, blending your requests in seamlessly. A do-not-play list is just as welcome.</div></details>
      <details><summary>How interactive is the MC?</summary><div class="a">As interactive as you want. Our MCs can drive a night of non-stop energy or stay in the background and keep the attention on you.</div></details>
      <details><summary>Can you handle the ceremony too?</summary><div class="a">Yes. Silver and up include a separate ceremony and cocktail hour setup so every moment of your day is covered.</div></details>
    </div>
    <div style="margin-top:20px"><a class="btn btn-ghost" href="faq.html">All questions {ICON_ARROW}</a></div>
  </div>
</section>

{cta_band("Your date is the first thing we check.", "Peak Saturdays go months ahead. Send us the date and venue and we'll confirm availability and send a quote within 24 to 72 hours.")}
'''
