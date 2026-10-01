from partials import *

FILENAME = "about.html"
TITLE = "About DJ Kastro · SoManyStylez Entertainment"
DESC = "Meet Robert Douriet, DJ Phidel Kastro, the Cuban Turntable Assassin. From Lakewood house parties and a bar residency to Jersey Club production and founding SoManyStylez Entertainment in 2014."

BODY = page_hero(
    "About",
    "The Cuban <span class=\"grad\">Turntable</span> Assassin.",
    "Robert Douriet, better known as DJ Phidel Kastro, is the founder, owner and lead DJ of SoManyStylez Entertainment. This is how he got here.",
    "assets/img/dj-kastro-decks.jpg",
    crumbs="<span>About</span>", cta=False) + f'''

<section class="section">
  <div class="wrap split">
    <div class="split-media tall"><img src="assets/img/dj-kastro-turntables.jpg" alt="DJ Kastro at the turntables" loading="lazy"></div>
    <div class="split-copy">
      <span class="eyebrow">The story</span>
      <h2>From house parties to hundreds of weddings.</h2>
      <p class="lead">Kastro grew up in Lakewood, New Jersey, pulled in by dozens of artists and genres until DJing was the only answer. He started with local house parties, then became the resident DJ at Cheeques, the bar featured in the film <em>The Wrestler</em>, shaking the building every night.</p>
      <p style="color:var(--fg-2)">Wanting to understand how records were made, he picked up FL Studio and dove into the Jersey Club scene, producing blends and tracks and collaborating with artists across Hip Hop, Dance and House. His musical background runs through Hip Hop, R&amp;B, Club, House, Dance, Reggae and Reggaeton, and he still produces today.</p>
      <p style="color:var(--fg-2)">As the private events came, weddings, proms, baby showers, he knocked each one out of the park and built the musical vocabulary to work any era and any genre. In 2014 he formed SoManyStylez, SMS Entertainment, and it has been nothing but up from there.</p>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Timeline</span><h2>How SMS came together.</h2></div>
    <div class="grid-4">
      <div class="step reveal"><span class="k">THE START</span><h4>Lakewood house parties</h4><p>Learning to read a room before there was a room to read.</p></div>
      <div class="step reveal" data-delay="1"><span class="k">THE RESIDENCY</span><h4>Cheeques</h4><p>Resident DJ at the bar featured in <em>The Wrestler</em>. Every night, packed.</p></div>
      <div class="step reveal" data-delay="2"><span class="k">THE STUDIO</span><h4>Jersey Club producer</h4><p>FL Studio, blends and collaborations with artists across Hip Hop, Dance and House.</p></div>
      <div class="step reveal" data-delay="3"><span class="k">2014</span><h4>SoManyStylez founded</h4><p>Countless events later, no event is too big or too small.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="pull reveal">Our mission is to deliver the memorable moments that lead to new and old memories, with <em>authenticity, originality and pride.</em></p>
    <p class="lead reveal" style="margin-top:22px">Remember: there is entertainment, and then there is an experience. It's our ability to provide a quality atmosphere and professionalism for any occasion that sets SoManyStylez apart. A truly unforgettable experience.</p>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">What we stand on</span><h2>Three promises, every event.</h2></div>
    <div class="pillars">
      <div class="pillar reveal"><span class="n">01</span><h3>Professionalism</h3><p>Your wedding or special event runs smoothly from beginning to end. Every SMS DJ has over a decade of professional DJ and MC experience.</p></div>
      <div class="pillar reveal" data-delay="1"><span class="n">02</span><h3>Affordability</h3><p>An unforgettable night within your budget. You deserve an affordable DJ without jeopardizing the success of your event.</p></div>
      <div class="pillar reveal" data-delay="2"><span class="n">03</span><h3>Reliability</h3><p>You'll never have to worry about your DJ not showing up on your big day. Our DJs are trustworthy, prepared and ready to serve you.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split rev">
    <div class="split-media"><img src="assets/img/dj-setup-totems.jpg" alt="DJ Kastro at the SoManyStylez booth with screens and totems" loading="lazy"></div>
    <div class="split-copy">
      <span class="eyebrow">The team</span>
      <h2>Kastro, plus the people behind the booth.</h2>
      <p class="lead">SoManyStylez is a family business. Kastro's wife runs the SMS Selfie PhotoBooths, and every DJ and MC on the roster brings more than a decade of professional experience. Based in Jackson, NJ, serving all of New Jersey, Pennsylvania and Delaware.</p>
      <div class="stats">
        <div class="stat"><b class="grad">5.0</b><span>WeddingWire &amp; The Knot</span></div>
        <div class="stat"><b>2014</b><span>Founded</span></div>
      </div>
      {socials()}
    </div>
  </div>
</section>

{cta_band("Let's talk about your night.", "Call, text or send the form. Kastro reads every message himself.")}
'''
