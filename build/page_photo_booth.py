from partials import *

FILENAME = "photo-booth.html"
TITLE = "SMS Selfie PhotoBooths · SoManyStylez Entertainment"
DESC = "Open-air DSLR photo booths in NJ, PA and DE. Unlimited prints, instant text and email sharing, GIFs and boomerangs, custom templates, formal-wear attendant. LED wall and enclosure add-ons."

BOOTHS = [
    ("SMS Selfie Booth (Classic)", "Classic touchscreen open-air booth. The one everyone knows how to use."),
    ("SMS Selfie Social Booth", "Sleek, modern and built for sharing. Text, email and social in one tap."),
    ("SMS Selfie Booth V2 (LED)", "Classy and elegant, with LED trim that lights up in any color to match your theme."),
    ("SMS Infinite Booth (LED)", "Built to power the latest in photo booth tech: three-camera system, bounce-card lighting and LED trim."),
]

FAQS = [
    ("Do you print two photo strips?", "Our open-air DSLR booths print multiple copies, one for everyone in the booth. Our attendant helps separate the strips so every guest leaves with theirs."),
    ("Are the photos unlimited?", "Of course. Unlimited prints are included in all of our packages. Guests will have plenty of time to create their perfect pics."),
    ("Can we put a message or logo on each strip?", "Absolutely, at no charge. We design a template to match your wedding colors, theme or invitation so the strips feel like part of the event."),
    ("Can we close the booth during dinner?", "Yes. We can set up and close the booth for dinner. Idle time does count toward your hours of unlimited use."),
    ("Will someone from SoManyStylez be at our event?", "Yes. A professional attendant in formal wear sets up, runs and removes the booth and is on hand to help guests all night."),
    ("What do we need to reserve the booth?", "A $150 deposit holds your date, with a seven-day refund window if your plans change."),
    ("How much room do you need?", "About 10 by 10 feet for the booth setup."),
    ("How long do prints take?", "About 10 to 15 seconds. By the time guests step out of the booth, the prints are usually waiting."),
    ("What printer do you use?", "A lab-quality dye-sublimation printer. No smudging, no grainy inkjet look, and prints that last."),
    ("How do we share the photos afterward?", "Every image and strip is sent via Google Drive and uploaded to our online gallery, where friends and family can download for free, tag to Facebook or order more prints."),
    ("We have a photographer. Why a booth?", "You need a photographer for the event itself. The booth is for your guests: let loose, be silly and keep a print. When you see Grandma in a feather boa blowing kisses at the camera, you'll know it was worth it."),
    ("Do you do corporate events?", "Yes. Corporate events are one of the many places you'll find an SMS Entertainment booth."),
]

def booths():
    return ''.join(f'<div class="card reveal" data-delay="{i%3}"><div class="card-body" style="padding:26px"><span class="eyebrow">Model 0{i+1}</span><h3 style="margin-top:8px">{n}</h3><p>{d}</p></div></div>' for i, (n, d) in enumerate(BOOTHS))

def faqs():
    return ''.join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in FAQS)

BODY = page_hero(
    "SMS Selfie PhotoBooths",
    "Unlimited prints. <span class=\"grad\">Instant</span> shares. Zero awkward.",
    "Open-air DSLR booths with a formal-wear attendant, custom templates and a backdrop included. Add it to any DJ package or book it on its own.",
    "assets/img/selfie-booth.jpg",
    crumbs="<span>Photo Booth</span>") + f'''

<section class="section">
  <div class="wrap split">
    <div class="split-media"><img src="assets/img/booth-prints.jpg" alt="Photo booth strips and prints on a table" loading="lazy"></div>
    <div class="split-copy">
      <span class="eyebrow">What's included</span>
      <h2>Everything your guests need to have fun.</h2>
      <ul>
        <li class="check">Unlimited use with a standard backdrop to suit your event</li>
        <li class="check">Instant text and email delivery of images, GIFs, boomerangs and video</li>
        <li class="check">Customized templates designed to match your event, at no charge</li>
        <li class="check">DSLR camera, unlimited props and on-site printing in 2x6 and 4x6</li>
        <li class="check">Online hosted gallery plus Google Drive delivery after the event</li>
        <li class="check">Attended by a professional in formal wear, or unattended if you prefer</li>
      </ul>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">The booths</span><h2>Four looks. Pick the one that fits the room.</h2></div>
    <div class="grid-2">{booths()}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head split reveal">
      <div><span class="eyebrow">Add-ons</span><h2 style="margin-top:12px">Make it a backdrop they'll line up for.</h2></div>
      <p class="lead">A standard backdrop is included with every package. Upgrade the whole scene with LED.</p>
    </div>
    <div class="grid-3">
      <div class="pkg reveal"><h3>Standard backdrop</h3><div class="price"><b>Included</b></div><ul><li>Chosen to suit your event</li><li>Comes with every package</li></ul></div>
      <div class="pkg reveal" data-delay="1"><h3>Backdrop Wall (LED)</h3><div class="price"><b class="tabular">+$125</b></div><ul><li>7 by 7 foot LED wall</li><li>Lights to any color</li></ul></div>
      <div class="pkg hot reveal" data-delay="2"><h3>Enclosure (LED)</h3><div class="price"><b class="tabular">+$150</b></div><ul><li>10 by 10 foot LED enclosure</li><li>A full glowing room inside your room</li></ul></div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">How it works</span><h2>Booked in three steps.</h2></div>
    <div class="steps">
      <div class="step reveal"><span class="k">01</span><h3>Reserve the date</h3><p>A $150 deposit holds it, with a seven-day refund window if plans change.</p></div>
      <div class="step reveal" data-delay="1"><span class="k">02</span><h3>Approve your template</h3><p>We design a strip to match your colors, theme or invitation and send it over for a yes.</p></div>
      <div class="step reveal" data-delay="2"><span class="k">03</span><h3>We handle the night</h3><p>Our attendant sets up in a 10 by 10 space, runs the booth and packs it all out.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head split reveal">
      <div><span class="eyebrow">See them in action</span><h2 style="margin-top:12px">Booth demos and event highlights.</h2></div>
      <p class="lead">Short clips from our YouTube channel. They open in a new tab.</p>
    </div>
    <div class="grid-4">{yt_cards()}</div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Photo booth questions</span><h2>Everything people ask us.</h2></div>
    <div class="faq">{faqs()}</div>
  </div>
</section>

{cta_band("Add the booth to your date.", "Tell us the event and we'll confirm booth availability and send pricing within 24 to 72 hours.")}
'''
