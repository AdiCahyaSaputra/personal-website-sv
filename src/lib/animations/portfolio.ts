import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export function animatePortfolio(node: HTMLElement) {
  gsap.registerPlugin(ScrollTrigger);
  const media = gsap.matchMedia(node);
  let disposed = false;

  media.add(
    {
      desktop:
        "(min-width: 1024px) and (min-height: 650px) and (hover: hover) and (pointer: fine)",
      motion: "(prefers-reduced-motion: no-preference)",
      reduced: "(prefers-reduced-motion: reduce)",
    },
    (context) => {
      if (context.conditions?.reduced) return;
      const desktop = context.conditions?.desktop;

      gsap
        .timeline({
          defaults: { ease: "power3.out" },
          scrollTrigger: {
            trigger: "hall",
            start: "top bottom",
            end: "bottom top",
            toggleActions: "play reverse play reverse",
          },
        })
        .from("[data-name-line]", {
          yPercent: 105,
          duration: 0.9,
          stagger: 0.12,
        })
        .from(
          "[data-hero-details]",
          { y: 16, opacity: 0, duration: 0.6 },
          0.35,
        );

      if (desktop) {
        gsap.to("#name", {
          y: 55,
          ease: "none",
          scrollTrigger: {
            trigger: "#about",
            start: "top top",
            end: "bottom top",
            scrub: 0.6,
          },
        });
      }

      // Keep the whole paragraph readable as the emphasis follows the scroll.
      gsap.from("[data-bio-word]", {
        opacity: 0.5,
        stagger: desktop ? 0.08 : 0.015,
        duration: 0.4,
        ease: "none",
        scrollTrigger: {
          trigger: "[data-profile]",
          start: "top 85%",
          end: desktop ? "bottom 65%" : "bottom top",
          scrub: desktop ? 0.35 : false,
          toggleActions: "play reverse play reverse",
        },
      });

      // Retain completed triggers until teardown so deep-link refreshes can initialize the pin safely.
      node
        .querySelectorAll<HTMLElement>("[data-section-intro]")
        .forEach((intro) => {
          gsap.from(intro.children, {
            y: 18,
            opacity: 0,
            duration: 0.55,
            stagger: 0.08,
            ease: "power2.out",
            scrollTrigger: {
              trigger: intro,
              start: "top 92%",
              toggleActions: "play reverse play reverse",
            },
          });
        });

      node
        .querySelectorAll<HTMLElement>("[data-project]")
        .forEach((project) => {
          const image = project.querySelector("[data-project-image]");
          gsap.from(project.querySelector("[data-project-copy]"), {
            x: desktop ? -24 : 0,
            y: desktop ? 0 : 16,
            opacity: 0,
            duration: 0.65,
            ease: "power2.out",
            scrollTrigger: {
              trigger: project,
              start: "top 88%",
              toggleActions: "play reverse play reverse",
            },
          });
          gsap.from(image, {
            clipPath: "inset(0 0 12% 0)",
            opacity: 0,
            duration: 0.8,
            ease: "power3.out",
            scrollTrigger: {
              trigger: image,
              start: "top 92%",
              toggleActions: "play reverse play reverse",
            },
          });
          if (desktop) {
            gsap.fromTo(
              project.querySelector("img"),
              { scale: 1.08, yPercent: 3 },
              {
                scale: 1,
                yPercent: -3,
                ease: "none",
                scrollTrigger: {
                  trigger: project,
                  start: "top bottom",
                  end: "bottom top",
                  scrub: 0.7,
                },
              },
            );
          }
        });

      node
        .querySelectorAll<HTMLElement>("[data-stack-group]")
        .forEach((group) => {
          gsap
            .timeline({
              defaults: { ease: "power2.out" },
              scrollTrigger: {
                trigger: group,
                start: "top 90%",
                toggleActions: "play reverse play reverse",
              },
            })
            .from(group.querySelector("h3"), {
              x: -12,
              opacity: 0,
              duration: 0.4,
            })
            .from(
              group.querySelectorAll("li"),
              {
                y: 14,
                opacity: 0,
                duration: 0.45,
                stagger: 0.055,
              },
              0.08,
            );
        });

      const experience = node.querySelector<HTMLElement>("#experience");
      const experienceIntro = node.querySelector<HTMLElement>(
        "[data-experience-intro]",
      );
      const roles = experience?.querySelector("ol");
      if (desktop && experienceIntro && roles) {
        ScrollTrigger.create({
          trigger: experienceIntro,
          start: "top 128px",
          endTrigger: roles,
          end: () => `bottom ${128 + experienceIntro.offsetHeight}px`,
          pin: true,
          pinSpacing: false,
          invalidateOnRefresh: true,
        });
      }
      node
        .querySelectorAll<HTMLElement>("[data-experience-row]")
        .forEach((row) => {
          gsap.from(row.children, {
            x: 18,
            opacity: 0,
            duration: 0.5,
            stagger: 0.07,
            ease: "power2.out",
            scrollTrigger: {
              trigger: row,
              start: "top 90%",
              toggleActions: "play reverse play reverse",
            },
          });
        });

      gsap
        .timeline({
          defaults: { ease: "power3.out" },
          scrollTrigger: {
            trigger: "#contact",
            start: "top 85%",
            toggleActions: "play reverse play reverse",
          },
        })
        .from("#contact-heading", {
          clipPath: "inset(0 0 100% 0)",
          y: 24,
          duration: 0.8,
        })
        .from("#contact p", { opacity: 0, duration: 0.5 }, 0.25)
        .from(
          "#contact li",
          { y: 16, opacity: 0, duration: 0.5, stagger: 0.09 },
          0.35,
        );
    },
  );

  // Font metrics affect pin boundaries and scroll positions on a cold load.
  void document.fonts.ready.then(() => {
    if (!disposed) ScrollTrigger.refresh();
  });

  return () => {
    disposed = true;
    media.revert();
  };
}
