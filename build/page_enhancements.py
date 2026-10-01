from partials import *

FILENAME = "enhancements.html"
TITLE = "Event Enhancements · SoManyStylez Entertainment"
DESC = "Dancing on a cloud, glow totems, uplighting, monogram gobos, cold sparks, premium giveaways, SMS Visualz, Snapchat geofilters and more. Event enhancements from SoManyStylez Entertainment, NJ."

ENH = [
    ("assets/img/dancing-on-a-cloud.jpg", "Weddings", "Dancing On A Cloud", "Low-lying fog that creates a fairytale atmosphere for your first dance. It stays at your feet and clears fast."),
    ("assets/img/glow-totems.jpg", "Lighting", "Glow Totems", "Pillars of light lining the booth or the room, matched to any color in your palette."),
    ("assets/img/uplighting.jpg", "Lighting", "Enhance Your Elegance", "Uplighting that creates a more beautiful atmosphere in any venue. Pick a color, or shift through the night."),
    ("assets/img/monogram-gobo.jpg", "Personal touch", "Monogram Gobo", "Your names, date or logo projected onto the dance floor or wall. Custom designed for you."),
    ("assets/img/cold-sparks.jpg", "Wow moment", "Cold Sparks", "Indoor-safe spark fountains for the grand entrance, the first dance or the last song."),
    ("assets/img/glow-giveaways.jpg", "Crowd", "Premium Giveaways", "We're talking glow tubes, not sticks and gizmos. Glow batons, hats, leis and sunglasses for the whole floor."),
    ("assets/img/selfie-booth.jpg", "Guests", "SMS Selfie PhotoBooths", "Open-air DSLR booths with unlimited prints, instant sharing and custom templates."),
    ("assets/img/dj-setup-totems.jpg", "Screens", "SoManyStylez Visualz", "Display slideshows, videos, pictures and social media on screens at the booth or around the room. Anything a computer can display, we can show your guests."),
    ("assets/img/snapchat-geofilter.jpg", "Social", "Snapchat Geofilter", "A digital picture frame perfectly designed for your event, live on Snapchat at your venue."),
    ("assets/img/prom-crowd.jpg", "Energy", "Game / Dance Motivator", "A motivator keeps the schedule flowing and the floor full, from line dances to the last call."),
    ("assets/img/ceremony.jpg", "Weddings", "Ceremony & Cocktail Hour", "A separate sound setup and a mic'd officiant, so every word and every song lands."),
    ("assets/img/dj-kastro-mic.jpg", "Crew", "Additional DJ / Emcee", "Add a second DJ or a dedicated MC. Trained and fun staff creates smooth entertainment."),
    ("assets/img/dj-kastro-booth.jpg", "Time", "Additional Hours", "The party doesn't stop when the clock says so. Extend the night by the hour."),
    ("assets/img/audio-guestbook.jpg", "Keepsake", "Audio Guestbook", "A vintage phone your guests pick up to leave a voicemail you'll keep forever."),
    ("assets/img/led-facade.jpg", "Decor", "LED Façades", "Table-top or full-panel LED DJ façades that glow in your colors."),
]

def cards():
    out = []
    for i, (img, tag, name, desc) in enumerate(ENH):
        im = f'<img src="{img}" alt="{name}" loading="lazy">' if img else ''
        cls = ' no-img' if not img else ''
        out.append(f'<div class="enh{cls} reveal" data-delay="{i%3}">{im}<div class="enh-body"><span class="tag">{tag}</span><h3>{name}</h3><p>{desc}</p></div></div>')
    return ''.join(out)

BODY = page_hero(
    "Event enhancements",
    "Turn a party into a <span class=\"grad\">production.</span>",
    "Every enhancement can be added to any package, for any event. Mix lighting, effects and keepsakes until the room looks like the one you pictured.",
    "assets/img/glow-totems.jpg",
    crumbs="<span>Enhancements</span>") + f'''

<section class="section">
  <div class="wrap">
    <div class="enh-grid">{cards()}</div>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Popular combinations</span><h2>What people pair together.</h2></div>
    <div class="grid-3">
      <div class="card reveal"><div class="card-body" style="padding:26px"><span class="eyebrow">Weddings</span><h3 style="margin-top:8px">The fairytale</h3><p>Dancing on a cloud, monogram gobo, uplighting and cold sparks for the last dance.</p><a class="more" href="weddings.html">Wedding packages {ICON_ARROW}</a></div></div>
      <div class="card reveal" data-delay="1"><div class="card-body" style="padding:26px"><span class="eyebrow">Sweet 16s</span><h3 style="margin-top:8px">The glow-up</h3><p>Glow totems, premium giveaways, LED façade and the selfie booth with an LED enclosure.</p><a class="more" href="events.html#sweet16">Sweet 16 packages {ICON_ARROW}</a></div></div>
      <div class="card reveal" data-delay="2"><div class="card-body" style="padding:26px"><span class="eyebrow">Corporate</span><h3 style="margin-top:8px">The brand night</h3><p>SMS Visualz with your logo, a branded photo booth template and a Snapchat geofilter.</p><a class="more" href="events.html#corporate">Corporate events {ICON_ARROW}</a></div></div>
    </div>
  </div>
</section>

{cta_band("Build your night.", "Tell us the event and the enhancements you're eyeing. We'll quote the full picture within 24 to 72 hours.")}
'''
