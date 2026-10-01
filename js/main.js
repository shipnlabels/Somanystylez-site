/* SoManyStylez Entertainment — shared behaviour */
(function () {
  const d = document;
  d.documentElement.classList.add('js');

  /* always open a page at the top (embedded viewers can carry the previous page's scroll position over) */
  try { if ('scrollRestoration' in history) history.scrollRestoration = 'manual'; } catch (e) {}
  const toTop = () => { if (!location.hash) { d.documentElement.style.scrollBehavior = 'auto'; window.scrollTo(0, 0); requestAnimationFrame(() => d.documentElement.style.scrollBehavior = ''); } };
  toTop();
  window.addEventListener('pageshow', toTop);
  window.addEventListener('load', toTop);

  /* header state */
  const header = d.querySelector('.site-header');
  const onScroll = () => {
    if (header) header.classList.toggle('scrolled', window.scrollY > 24);
    const bar = d.querySelector('.book-bar');
    if (bar) bar.classList.toggle('show', window.scrollY > 420);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
  if (d.querySelector('.book-bar')) d.body.classList.add('has-bar');

  /* mobile menu */
  const menuBtn = d.querySelector('.menu-btn');
  const menu = d.querySelector('.menu');
  if (menuBtn && menu) {
    menu.querySelectorAll('li').forEach((li, i) => li.style.setProperty('--i', i));
    const setOpen = (open) => {
      d.body.classList.toggle('menu-open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
      menu.setAttribute('aria-hidden', String(!open));
    };
    menuBtn.addEventListener('click', () => setOpen(!d.body.classList.contains('menu-open')));
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
    d.addEventListener('keydown', e => { if (e.key === 'Escape') setOpen(false); });
  }

  /* reveal on scroll (elements start visible without JS; with JS they fade up) */
  const items = d.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && items.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(el => io.observe(el));
    /* anything already in view on load */
    requestAnimationFrame(() => items.forEach(el => { const r = el.getBoundingClientRect(); if (r.top < window.innerHeight) el.classList.add('in'); }));
  } else {
    items.forEach(el => el.classList.add('in'));
  }

  /* feature video: poster + play button → plays with sound */
  d.querySelectorAll('.feature-video').forEach(box => {
    const v = box.querySelector('video');
    const play = box.querySelector('.play');
    if (!v || !play) return;
    const start = () => {
      box.classList.add('playing');
      v.controls = true;
      v.muted = false;
      v.play().catch(() => { v.muted = true; v.play().catch(() => {}); });
    };
    play.addEventListener('click', start);
    v.addEventListener('ended', () => { box.classList.remove('playing'); v.controls = false; v.currentTime = 0; });
  });

  /* pause the hero loop when it scrolls away (saves battery on phones) */
  const heroVid = d.querySelector('.hero-media video');
  if (heroVid && 'IntersectionObserver' in window) {
    new IntersectionObserver((en) => {
      en.forEach(e => { if (e.isIntersecting) heroVid.play().catch(() => {}); else heroVid.pause(); });
    }, { threshold: 0.05 }).observe(heroVid);
  }

  /* equalizer bars */
  d.querySelectorAll('.eq').forEach(eq => {
    const n = 28;
    for (let i = 0; i < n; i++) {
      const b = d.createElement('i');
      b.style.animationDelay = (Math.random() * -1.4) + 's';
      b.style.animationDuration = (0.9 + Math.random() * 0.9) + 's';
      b.style.opacity = (0.55 + Math.random() * 0.45).toFixed(2);
      eq.appendChild(b);
    }
  });

  /* copy buttons */
  d.querySelectorAll('[data-copy]').forEach(btn => {
    btn.addEventListener('click', () => {
      const text = btn.getAttribute('data-copy');
      const done = () => { const o = btn.textContent; btn.textContent = 'Copied'; setTimeout(() => btn.textContent = o, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done).catch(() => fallback());
      else fallback();
      function fallback() {
        const ta = d.createElement('textarea'); ta.value = text; d.body.appendChild(ta); ta.select();
        try { d.execCommand('copy'); done(); } catch (e) {} d.body.removeChild(ta);
      }
    });
  });

  /* contact form: builds a prefilled email to the business and opens the visitor's mail app.
     A fallback panel offers text / copy in case the device has no mail app set up. */
  const form = d.querySelector('#booking-form');
  if (form) {
    const TO = 'SoManyStylezEnt@gmail.com';
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const f = new FormData(form);
      const addons = f.getAll('addons');
      const subject = `Availability request: ${f.get('type') || 'Event'}${f.get('date') ? ' on ' + f.get('date') : ''}`;
      const body = [
        `Hi DJ Kastro,`,
        ``,
        `I'd like to check availability for my event.`,
        ``,
        `Name: ${f.get('name') || ''}`,
        `Phone: ${f.get('phone') || ''}`,
        `Email: ${f.get('email') || ''}`,
        `Event type: ${f.get('type') || ''}`,
        `Event date: ${f.get('date') || 'TBD'}`,
        `Venue / town: ${f.get('venue') || 'TBD'}`,
        `Guest count: ${f.get('guests') || 'TBD'}`,
        `Interested in: ${addons.length ? addons.join(', ') : 'DJ / MC'}`,
        ``,
        `About the night:`,
        `${f.get('message') || ''}`,
        ``,
        `Sent from somanystylezentertainment.com`
      ].join('\n');
      const mailto = 'mailto:' + TO + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      const out = d.querySelector('#form-out');
      const txt = d.querySelector('#form-text');
      const sms = d.querySelector('#send-sms');
      const mail = d.querySelector('#send-mail');
      const copy = d.querySelector('#copy-form');
      if (txt) txt.textContent = body;
      if (mail) mail.href = mailto;
      if (sms) sms.href = 'sms:+16097820269?&body=' + encodeURIComponent(body);
      if (copy) copy.setAttribute('data-copy', body);
      if (out) { out.hidden = false; out.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
      /* open the prefilled email */
      try { window.location.href = mailto; } catch (err) {}
    });
  }

  /* current year */
  d.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
})();
