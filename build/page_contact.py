from partials import *

FILENAME = "contact.html"
TITLE = "Check Availability · SoManyStylez Entertainment"
DESC = "Check your date with SoManyStylez Entertainment. Call or text (609) 782-0269, email, or send the booking form. Based in Jackson, NJ, serving NJ, PA and DE."

TYPES = ["Wedding", "Sweet 16 / Quinceañera", "Prom / School event", "Birthday", "Anniversary", "Corporate / Holiday party", "Private party", "Other"]
ADDONS = ["SMS Selfie PhotoBooth", "Dancing On A Cloud", "Uplighting", "Monogram Gobo", "Glow Totems", "Cold Sparks", "Premium Giveaways", "SMS Visualz"]

BODY = page_hero(
    "Contact",
    "Let's check <span class=\"grad\">your date.</span>",
    "Call, text, email or send the form. Please allow 24 to 72 hours for a response, though it's usually much faster.",
    "assets/img/still-booth-guests.jpg",
    crumbs="<span>Contact</span>", cta=False) + f'''

<section class="section">
  <div class="wrap grid-2" style="align-items:start;gap:28px">
    <div class="contact-card reveal">
      <div class="contact-line"><small>Call or text</small><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><button class="copy-btn" data-copy="(609) 782-0269">Copy number</button></div>
      <div class="contact-line"><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a><button class="copy-btn" data-copy="{EMAIL}">Copy email</button></div>
      <div class="contact-line"><small>Based in</small><span class="big">Jackson, New Jersey</span><span class="muted" style="font-size:.9rem">Serving all of NJ, PA and DE</span></div>
      <div class="contact-line"><small>Response time</small><span class="big">24 to 72 hours</span></div>
      <div class="contact-line"><small>Follow</small>{socials()}</div>
      <div class="contact-line"><small>Quick links</small><div class="chips"><a class="chip" href="weddings.html">Wedding tiers</a><a class="chip" href="events.html#sweet16">Sweet 16 prices</a><a class="chip" href="photo-booth.html">Booth add-ons</a></div></div>
    </div>

    <form class="form reveal" id="booking-form" novalidate>
      <div class="row">
        <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" required placeholder="First and last"></div>
        <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder="(609) 555-0100"></div>
      </div>
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required placeholder="you@example.com"></div>
      <div class="row">
        <div class="field"><label for="f-type">Event type</label><select id="f-type" name="type">{''.join(f'<option>{t}</option>' for t in TYPES)}</select></div>
        <div class="field"><label for="f-date">Event date</label><input id="f-date" name="date" type="date"></div>
      </div>
      <div class="row">
        <div class="field"><label for="f-venue">Venue or town</label><input id="f-venue" name="venue" type="text" placeholder="Venue name or town"></div>
        <div class="field"><label for="f-guests">Guest count</label><input id="f-guests" name="guests" type="number" min="1" inputmode="numeric" placeholder="About how many"></div>
      </div>
      <fieldset class="field" style="border:0;padding:0;margin:0"><legend style="font-size:.82rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--fg-2);margin-bottom:8px">Interested in</legend>
        <div class="chips">{''.join(f'<label class="chip" style="cursor:pointer;display:inline-flex;gap:8px;align-items:center"><input type="checkbox" name="addons" value="{a}" id="f-addon-{i}" style="accent-color:#cf5cf2;margin:0">{a}</label>' for i, a in enumerate(ADDONS))}</div>
      </fieldset>
      <div class="field"><label for="f-msg">Tell us about the night</label><textarea id="f-msg" name="message" placeholder="The vibe, must-play songs, timeline, anything we should know."></textarea></div>
      <button class="btn btn-primary" type="submit" style="justify-self:start">Send availability request {ICON_ARROW}</button>
      <p class="form-note">Opens a prefilled email to {EMAIL} in your mail app. Prefer to text? Use the button below after sending.</p>
      <div class="form-sent" id="form-out" hidden>
        <strong>Your email should have opened. If it didn't, use one of these:</strong>
        <pre id="form-text" style="white-space:pre-wrap;font:inherit;font-size:.92rem;color:var(--fg-2);margin:0"></pre>
        <div class="hero-cta">
          <a class="btn btn-primary btn-sm" id="send-mail" href="mailto:{EMAIL}">Open email again</a>
          <a class="btn btn-ghost btn-sm" id="send-sms" href="sms:{PHONE_TEL}">{ICON_MSG} Text it instead</a>
          <button class="btn btn-ghost btn-sm" type="button" id="copy-form" data-copy="">Copy the message</button>
        </div>
      </div>
    </form>
  </div>
</section>

<section class="section band">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">What happens next</span><h2>Three steps to a locked date.</h2></div>
    <div class="steps">
      <div class="step reveal"><span class="k">01</span><h3>We confirm the date</h3><p>You hear back within 24 to 72 hours with availability and a quote based on your package and add-ons.</p></div>
      <div class="step reveal" data-delay="1"><span class="k">02</span><h3>Deposit holds it</h3><p>A deposit locks your date. Photo booth deposits have a seven-day refund window.</p></div>
      <div class="step reveal" data-delay="2"><span class="k">03</span><h3>We plan the night</h3><p>Song request sheet, do-not-play list, timeline and template approvals, all before the day.</p></div>
    </div>
  </div>
</section>
'''
