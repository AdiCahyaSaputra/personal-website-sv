<script lang="ts">
  import { gsap } from "gsap";
  import { ScrollTrigger } from "gsap/ScrollTrigger";
  import Navigation from "@/components/reusable/navigation.svelte";
  import HallSection from "@/components/section/hall-section.svelte";
  import ProfileSection from "@/components/section/profile-section.svelte";
  import ProjectSection from "@/components/section/project-section.svelte";
  import TechStackSection from "@/components/section/tech-stack-section.svelte";
  import ExperienceSection from "@/components/section/experience-section.svelte";
  import ContactSection from "@/components/section/contact-section.svelte";

  function animatePage(node: HTMLElement) {
    gsap.registerPlugin(ScrollTrigger);
    const media = gsap.matchMedia();
    media.add("(prefers-reduced-motion: no-preference)", () => {
      const context = gsap.context(() => {
        gsap.from("[data-intro]", {
          y: 35,
          opacity: 0,
          duration: 0.85,
          stagger: 0.1,
          ease: "power3.out",
          clearProps: "all",
        });
        node
          .querySelectorAll<HTMLElement>("[data-reveal]")
          .forEach((element) => {
            gsap.from(element, {
              y: 24,
              opacity: 0,
              duration: 0.65,
              ease: "power2.out",
              clearProps: "all",
              scrollTrigger: { trigger: element, start: "top 94%", once: true },
            });
          });
      }, node);
      return () => context.revert();
    });
    return () => media.revert();
  }
</script>

<a
  class="fixed top-3 left-5 z-40 -translate-y-[200%] bg-white px-5 py-3 text-black focus:translate-y-0"
  href="#main">Skip to content</a
>
<Navigation />
<main id="main" tabindex="-1" {@attach animatePage}>
  <HallSection />
  <ProfileSection />
  <ProjectSection />
  <TechStackSection />
  <ExperienceSection />
  <ContactSection />
</main>
