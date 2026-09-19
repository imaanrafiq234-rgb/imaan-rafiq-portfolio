/* =====================================================================
   Imaan Rafiq — Portfolio interactions
   ===================================================================== */
(function () {
  "use strict";

  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Mobile nav ---------- */
  const toggle = $(".nav__toggle");
  const links  = $(".nav__links");
  if (toggle && links) {
    toggle.addEventListener("click", () => {
      const open = links.dataset.open === "true";
      links.dataset.open = String(!open);
      toggle.textContent = open ? "Menu" : "Close";
      toggle.setAttribute("aria-expanded", String(!open));
    });
    $$(".nav__link", links).forEach((a) =>
      a.addEventListener("click", () => {
        links.dataset.open = "false";
        toggle.textContent = "Menu";
      })
    );
  }

  /* ---------- Scroll progress ---------- */
  const bar = $(".progress");
  if (bar) {
    const onScroll = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + "%";
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Reveal on scroll ---------- */
  const revealables = $$("[data-reveal]");
  if (revealables.length) {
    if (reduce || !("IntersectionObserver" in window)) {
      revealables.forEach((el) => el.classList.add("is-in"));
    } else {
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((e) => {
            if (e.isIntersecting) {
              e.target.classList.add("is-in");
              io.unobserve(e.target);
            }
          });
        },
        { rootMargin: "0px 0px -12% 0px", threshold: 0.08 }
      );
      revealables.forEach((el) => io.observe(el));
    }
  }

  /* ---------- Stagger children of a group ---------- */
  $$("[data-stagger]").forEach((group) => {
    const step = parseInt(group.dataset.stagger, 10) || 90;
    $$(":scope > [data-reveal]", group).forEach((el, i) => {
      el.style.setProperty("--d", i * step + "ms");
    });
  });

  /* ---------- Work filters ---------- */
  const filterBar = $("[data-filters]");
  if (filterBar) {
    const cards = $$("[data-tags]");
    const apply = (f) => {
      cards.forEach((c) => {
        const tags = (c.dataset.tags || "").split(/\s+/);
        const show = f === "all" || tags.includes(f);
        c.hidden = !show;
        if (show) {
          c.classList.remove("is-in");
          void c.offsetWidth;
          c.classList.add("is-in");
        }
      });
    };
    filterBar.addEventListener("click", (e) => {
      const chip = e.target.closest(".chip");
      if (!chip) return;
      $$(".chip", filterBar).forEach((c) => c.setAttribute("aria-pressed", String(c === chip)));
      apply(chip.dataset.filter);
      history.replaceState(null, "", chip.dataset.filter === "all" ? location.pathname : "#" + chip.dataset.filter);
    });
    const hash = location.hash.replace("#", "");
    const initial = filterBar.querySelector(`.chip[data-filter="${hash}"]`);
    if (initial) initial.click();
  }

  /* ---------- Lightbox ---------- */
  const lb = $(".lightbox");
  if (lb) {
    const img    = $("img", lb);
    const shots  = $$("[data-lightbox]");
    let idx = 0, lastFocus = null;

    const show = (i) => {
      idx = (i + shots.length) % shots.length;
      const source = $("img", shots[idx]);
      img.src = source.currentSrc || source.src;
      img.alt = source.alt || "";
      const counter = $(".lightbox__count", lb);
      if (counter) counter.textContent = `${idx + 1} / ${shots.length}`;
    };
    const open = (i) => {
      lastFocus = document.activeElement;
      show(i);
      lb.dataset.open = "true";
      lb.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
      $(".lightbox__close", lb).focus();
    };
    const close = () => {
      lb.dataset.open = "false";
      lb.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
      img.src = "";
      if (lastFocus) lastFocus.focus();
    };

    shots.forEach((s, i) => s.addEventListener("click", () => open(i)));
    $(".lightbox__close", lb).addEventListener("click", close);
    $(".lightbox__prev", lb)?.addEventListener("click", () => show(idx - 1));
    $(".lightbox__next", lb)?.addEventListener("click", () => show(idx + 1));
    lb.addEventListener("click", (e) => { if (e.target === lb) close(); });

    document.addEventListener("keydown", (e) => {
      if (lb.dataset.open !== "true") return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
    });

    // swipe
    let x0 = null;
    lb.addEventListener("touchstart", (e) => (x0 = e.touches[0].clientX), { passive: true });
    lb.addEventListener("touchend", (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }

  /* ---------- Year ---------- */
  $$("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));
})();