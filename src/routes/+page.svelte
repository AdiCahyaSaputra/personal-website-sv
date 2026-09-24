<script lang="ts">
  import { onMount } from "svelte";
  import { gsap } from "gsap";
  import { ScrollTrigger } from "gsap/ScrollTrigger";
  import { PROJECTS } from "$lib/constants/projects";
  import { TECH_STACKS } from "$lib/constants/skill";

  const experience = [
    { role: "Full Stack Developer", company: "Crosva", period: "2025 — 2026", detail: "Built Yufo Trade across mobile, web, and backend services, and developed Twillink’s core application." },
    { role: "Full Stack Developer", company: "PT Enakans Media Teknologi", period: "2024 — 2026", detail: "Worked on order capture, billing, Oracle reporting, and the experience of internal dashboard tools." },
    { role: "Junior Software Engineer", company: "PT Pertamina Bina Medika IHC", period: "2024", detail: "Translated clinic needs into software and refactored the SIM Clinic application." },
    { role: "Full Stack Web Developer", company: "Mitrain ID", period: "2023 — 2024", detail: "Built a responsive B2B website with a focus on making it easier to use." },
    { role: "IT Support", company: "Pangeran Wijaya Kusuma School", period: "2023 — 2024", detail: "Kept the school network running and supported the equipment behind classes and events." }
  ];

  let page: HTMLElement;

  onMount(() => {
    gsap.registerPlugin(ScrollTrigger);
    const motion = gsap.matchMedia();
    const context = gsap.context(() => {
      motion.add("(prefers-reduced-motion: no-preference)", () => {
        gsap.fromTo(".scroll-progress", { scaleX: 0 }, {
          scaleX: 1, ease: "none",
          scrollTrigger: { trigger: page, start: "top top", end: "bottom bottom", scrub: 0.35 }
        });
        const intro = gsap.timeline({ defaults: { ease: "power3.out" } });
        intro
          .from(".hero-line > span", { yPercent: 110, rotate: 3, duration: 1.15, stagger: 0.13 })
          .from(".hero-intro, .hero-meta, .hero-mark", { y: 34, opacity: 0, duration: 0.8, stagger: 0.12 }, "-=0.58");

        gsap.to(".hero-mark", {
          rotate: 28, yPercent: 25, ease: "none",
          scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: 1 }
        });

        gsap.utils.toArray<HTMLElement>("[data-reveal]").forEach((element) => {
          gsap.from(element, {
            y: 70, opacity: 0, duration: 1, ease: "power3.out",
            scrollTrigger: { trigger: element, start: "top 85%", once: true }
          });
        });

        gsap.utils.toArray<HTMLElement>(".experience-row").forEach((element) => {
          gsap.from(element, {
            y: 28, opacity: 0, duration: 0.7, ease: "power2.out",
            scrollTrigger: { trigger: element, start: "top 88%", once: true }
          });
        });

        gsap.from(".skill-item", {
          y: 28, opacity: 0, duration: 0.55,
          stagger: { amount: 1.15, from: "start" }, ease: "power2.out",
          scrollTrigger: { trigger: ".skills-grid", start: "top 82%", once: true }
        });
      });

      motion.add("(min-width: 900px) and (prefers-reduced-motion: no-preference)", () => {
        const cards = gsap.utils.toArray<HTMLElement>(".project-panel");
        const last = cards[cards.length - 1];
        if (!last) return;

        cards.slice(0, -1).forEach((card, index) => {
          const next = cards[index + 1];
          ScrollTrigger.create({
            trigger: card, start: "top top", endTrigger: last, end: "top top",
            pin: true, pinSpacing: false, invalidateOnRefresh: true
          });
          gsap.to(card.querySelector(".project-inner"), {
            scale: 0.93, opacity: 0.55, ease: "none",
            scrollTrigger: { trigger: next, start: "top bottom", end: "top top", scrub: true }
          });
        });
      });
    }, page);

    return () => {
      motion.revert();
      context.revert();
    };
  });
</script>

<svelte:head>
  <title>Adi Cahya Saputra — Full Stack Developer</title>
  <meta name="description" content="Adi Cahya Saputra is a full stack developer in Jakarta building useful web and mobile products." />
  <meta property="og:title" content="Adi Cahya Saputra — Full Stack Developer" />
  <meta property="og:description" content="Building useful web and mobile products from Jakarta, Indonesia." />
</svelte:head>

<main bind:this={page}>
  <div class="scroll-progress" aria-hidden="true"></div>
  <section class="hero" id="top" aria-labelledby="hero-title">
    <header class="site-header page-gutter">
      <a class="wordmark" href="#top" aria-label="Adi Cahya Saputra, back to top">ACS<span>®</span></a>
      <nav aria-label="Main navigation">
        <a href="#about">About</a>
        <a href="#work">Work</a>
        <a href="#experience">Experience</a>
      </nav>
      <a class="header-contact" href="mailto:adics631@gmail.com">Let's talk <span aria-hidden="true">↗</span></a>
    </header>

    <div class="hero-main page-gutter">
      <div class="hero-kicker hero-meta"><span class="status-dot" aria-hidden="true"></span> Full stack developer · Jakarta, Indonesia</div>
      <h1 id="hero-title">
        <span class="hero-line"><span>ADI CAHYA</span></span>
        <span class="hero-line hero-line-last"><span>SAPUTRA<span class="hero-period">.</span></span></span>
      </h1>
      <div class="hero-bottom">
        <p class="hero-intro">I build digital products<br />that <em>actually get used.</em></p>
        <div class="hero-mark" aria-hidden="true"><span>ACS</span><span class="hero-mark-cross">✳</span></div>
        <div class="hero-meta hero-side-note">WEB / MOBILE / PRODUCT<br />BASED IN NORTH JAKARTA</div>
      </div>
    </div>
    <div class="hero-footer page-gutter"><a href="https://www.linkedin.com/in/adi-cs/" target="_blank" rel="noreferrer">LINKEDIN ↗</a><span>JAKARTA, INDONESIA</span></div>
  </section>

  <section class="about section-pad page-gutter" id="about" aria-labelledby="about-title">
    <div class="section-label" data-reveal>About me <span class="label-line"></span></div>
    <div class="about-grid">
      <h2 id="about-title" data-reveal>FROM AN<br /><span>IDEA</span> TO A<br />REAL THING<span class="accent-period">.</span></h2>
      <div class="about-copy" data-reveal>
        <span class="asterisk" aria-hidden="true">✳</span>
        <p>I'm Adi, a full stack developer with a soft spot for good interfaces and the systems behind them.</p>
        <p>I started in software engineering at vocational school and have since worked on everything from clinic software and internal tools to commerce platforms across web and mobile.</p>
        <p class="about-note">Currently studying Informatics Engineering at Metaguna University. Still learning by building.</p>
        <a class="text-link" href="https://www.linkedin.com/in/adi-cs/" target="_blank" rel="noreferrer">More about me on LinkedIn <span aria-hidden="true">↗</span></a>
      </div>
    </div>
  </section>

  <section class="work section-pad" id="work" aria-labelledby="work-title">
    <div class="work-heading page-gutter">
      <div class="section-label section-label-light" data-reveal>Selected work <span class="label-line"></span></div>
      <div class="work-heading-grid">
        <h2 id="work-title" data-reveal>BUILT TO<br /><span>SHIP.</span></h2>
        <p data-reveal>Real products, real users, and the work between the first sketch and the live release.</p>
      </div>
    </div>
    <div class="project-stack">
      {#each PROJECTS as project, index}
        <article class:project-peach={index === 0} class:project-blue={index === 1} class="project-panel" aria-labelledby={"project-" + index}>
          <div class="project-inner page-gutter">
            <div class="project-topline"><span>FEATURED PROJECT / 0{index + 1}</span><span>{project.hashtag.includes("mobile") ? "WEB + MOBILE" : "WEB PLATFORM"}</span></div>
            <div class="project-content">
              <div class="project-copy">
                <h3 id={"project-" + index}>{project.title}</h3>
                <p>{project.description}</p>
                <div class="project-tags">{#each project.hashtag as tag}<span>{tag}</span>{/each}</div>
                {#if project.demoUrl}<a class="project-link" href={project.demoUrl} target="_blank" rel="noreferrer" aria-label={"Visit " + project.title + " website"}>Visit project <span aria-hidden="true">↗</span></a>{/if}
              </div>
              <div class="project-visual"><img src={project.imgUrl} alt={project.title + " product interface"} loading="lazy" /></div>
            </div>
          </div>
        </article>
      {/each}
    </div>
  </section>

  <section class="experience section-pad page-gutter" id="experience" aria-labelledby="experience-title">
    <div class="section-label" data-reveal>Where I've worked <span class="label-line"></span></div>
    <div class="experience-heading"><h2 id="experience-title" data-reveal>THE WORK<br /><span>BEHIND THE WORK.</span></h2><p data-reveal>Different teams. Different problems. One habit: make the thing work well for the people using it.</p></div>
    <div class="experience-list">
      {#each experience as item}
        <article class="experience-row"><span class="experience-period">{item.period}</span><div><h3>{item.role}</h3><span class="experience-company">{item.company}</span></div><p>{item.detail}</p><span class="experience-arrow" aria-hidden="true">↗</span></article>
      {/each}
    </div>
  </section>

  <section class="skills section-pad page-gutter" id="skills" aria-labelledby="skills-title">
    <div class="section-label" data-reveal>The toolkit <span class="label-line"></span></div>
    <div class="skills-heading"><h2 id="skills-title" data-reveal>TOOLS CHANGE.<br /><span>CURIOSITY STAYS.</span></h2><p data-reveal>These are the technologies and tools I keep close while building.</p></div>
    <ul class="skills-grid" aria-label="Technology stack">
      {#each TECH_STACKS as skill}
        <li class="skill-item"><img src={skill.icon} alt="" loading="lazy" /><span>{skill.name}</span></li>
      {/each}
    </ul>
  </section>

  <footer class="contact section-pad page-gutter" id="contact">
    <div class="section-label section-label-light" data-reveal>Have something in mind? <span class="label-line"></span></div>
    <p class="contact-lead" data-reveal>LET'S MAKE<br /><span>IT REAL.</span></p>
    <a class="contact-email" href="mailto:adics631@gmail.com">adics631@gmail.com <span aria-hidden="true">↗</span></a>
    <div class="footer-bottom"><span>© {new Date().getFullYear()} ADI CAHYA SAPUTRA</span><div><a href="https://www.linkedin.com/in/adi-cs/" target="_blank" rel="noreferrer">LINKEDIN ↗</a><a href="#top">BACK TO TOP ↑</a></div><span>MADE IN JAKARTA, INDONESIA</span></div>
  </footer>
</main>
