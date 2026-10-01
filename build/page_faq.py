from partials import *

FILENAME = "faq.html"
TITLE = "FAQ · SoManyStylez Entertainment"
DESC = "Answers about booking a SoManyStylez DJ: breaks, music requests, do-not-play lists, volume, light shows, MC interaction, gratuity, meals and photo booth details."

DJ = [
    ("Do you take breaks?", "Our DJ staff performs continuously throughout the night. From the scheduled start time until your party is over, the music is playing, unless you request a break for some other reason."),
    ("Can we choose the music played at our event?", "Our services are based solely on what you want them to be. Keeping a crowd alive depends on the type of music, the type of mix, DJ personality and atmosphere, not just the songs. Taking the time to fill out our SMS Song Request Sheet greatly increases the chances of a successful event and lets your DJ customize the music and blend your requests in seamlessly."),
    ("Can we have a do-not-play list?", "Yes. That list can be just as important to you and your event as the request list."),
    ("What if we want a song you don't have?", "Our collection spans the 50s through today. If a client wants something obscure we don't have, you can supply it on a flash drive before the event so we can preview and cue it, and we return the drive at the end of the night. Advance notice is appreciated if we need to track a song down."),
    ("How loud do you play the music?", "Sound is dispersed evenly through the venue so guests can hear each other and the background music. When it's time to dance we focus the music on the dance floor: loud enough to dance to on the floor, while the rest of the room can still socialize."),
    ("Do you provide a light show?", "Light shows are additional options. Your event coordinator will help you select one appropriate to your event. See the full list on our Enhancements page."),
    ("How interactive are your MCs and DJs?", "As interactive as you want them to be. Our DJs have the energy to elevate your event into a night of non-stop fun, or they can be background figures that keep the attention on your party, or any level in between."),
    ("Does the DJ expect a tip?", "It is not mandatory. If your DJ surpasses your expectations and you wish to tip, it is taken as a great compliment and truly appreciated."),
    ("Should we feed the DJ?", "Our DJs are often on site for six hours or more once setup and takedown are included. Please let us know whether you'll be providing a meal for the DJ staff so we can plan to pick something up on the way if not."),
    ("How far ahead should we book?", "As early as possible. Peak-season Saturdays fill months in advance. We're happy to check availability for any date at any time."),
    ("Where do you travel?", "We're based in Jackson, NJ and serve all of New Jersey, Pennsylvania and Delaware."),
]

PB = [
    ("What's required to reserve the photo booth?", "A $150 deposit holds your date, with a seven-day refund window if you change your mind."),
    ("How much room does the booth need?", "About 10 by 10 feet."),
    ("Are prints unlimited?", "Yes. Unlimited prints are included in every photo booth package, and our attendant helps hand them out."),
    ("Can we customize the photo strips?", "Yes, at no charge. We design a template to match your colors, theme or invitation."),
    ("How do we get the photos afterward?", "All images and strips are shared via Google Drive and posted to our online gallery for free downloads, Facebook tagging and reprints."),
]

def qa(items):
    return ''.join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in items)

BODY = page_hero(
    "FAQ",
    "Good <span class=\"grad\">questions.</span>",
    "Everything people ask before they book. If yours isn't here, call or message and we'll answer it directly.",
    "assets/img/dj-kastro-booth.jpg",
    crumbs="<span>FAQ</span>", cta=False) + f'''

<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">DJ &amp; MC</span><h2>The night itself.</h2></div>
    <div class="faq">{qa(DJ)}</div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Photo booth</span><h2>The booth.</h2></div>
    <div class="faq">{qa(PB)}</div>
    <div style="margin-top:20px"><a class="btn btn-ghost" href="photo-booth.html">All photo booth questions {ICON_ARROW}</a></div>
  </div>
</section>

{cta_band("Still have a question?", "Call, text or send the form. Kastro answers every message within 24 to 72 hours.")}
'''
