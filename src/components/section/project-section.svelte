<script lang="ts">
  import { gsap } from "gsap";
  import { ScrollTrigger } from "gsap/ScrollTrigger";
  import { PROJECTS } from "$lib/constants/projects";
  import { ArrowUpIcon, ArrowUpRightIcon } from "phosphor-svelte";

  function stackCards(node: HTMLElement) {
    gsap.registerPlugin(ScrollTrigger);

    const media = gsap.matchMedia();
    let disposed = false;

    media.add(
      "(min-width: 900px) and (min-height: 700px) and (prefers-reduced-motion: no-preference)",
      () => {
        const cards = Array.from(
          node.querySelectorAll<HTMLElement>("[data-stack-card]"),
        );

        cards.forEach((card, index) => {
          const next = cards[index + 1];
          const panel = card.querySelector<HTMLElement>("[data-card-panel]");

          ScrollTrigger.create({
            trigger: card,
            start: () => `top ${108 + index * 18}px`,
            endTrigger: "#work",
            end: () => {
              const lastCard = cards[cards.length - 1];
              const stackBottom =
                108 + (cards.length - 1) * 18 + lastCard.offsetHeight;

              return `clamp(bottom ${stackBottom}px)`;
            },
            pin: true,
            pinSpacing: false,
            invalidateOnRefresh: true,
          });

          if (next && panel) {
            gsap.to(panel, {
              scale: 1 - cards.length / 100 + index / 100, // len = 3, so it start 0.97, 0.98, 0.99
              transformOrigin: "50% 0%",
              ease: "none",
              scrollTrigger: {
                trigger: next,
                start: "top 85%",
                end: () => `top ${108 + (index + 1) * 18}px`,
                scrub: true,
                invalidateOnRefresh: true,
              },
            });
          }
        });
      },
    );

    void document.fonts.ready.then(() => {
      if (!disposed) ScrollTrigger.refresh();
    });

    return () => {
      disposed = true;
      media.revert();
    };
  }
</script>

<section id="work" class="bg-black" aria-label="Selected projects">
  <div class="md:px-10 px-4 pt-20 pb-30 max-[900px]:pt-12">
    <header
      class="mb-14 flex justify-center gap-8 max-[900px]:mb-8 max-[900px]:flex-col max-[900px]:items-start max-[900px]:gap-6"
    >
      <h2 class="mt-6 font-writer text-5xl md:text-8xl font-bold text-center">
        Project That I Proud <br />to Showcase
      </h2>
    </header>

    <div
      class="stack motion-safe:min-[900px]:[@media(min-height:700px)]:pb-[50vh]"
      {@attach stackCards}
    >
      {#each PROJECTS as project, index (project.title)}
        <article
          class={[
            "relative mb-4",
            index === PROJECTS.length - 1
              ? "motion-safe:min-[900px]:[@media(min-height:700px)]:mb-0"
              : "motion-safe:min-[900px]:[@media(min-height:700px)]:mb-8",
          ]}
          data-stack-card
          aria-labelledby={`stack-project-${index}`}
        >
          <div
            class="grid min-h-115 grid-cols-[1fr_1.35fr] overflow-hidden rounded-xl text-foreground motion-safe:min-[900px]:[@media(min-height:700px)]:h-[clamp(460px,64vh,640px)] max-[900px]:grid-cols-1 bg-background"
            data-card-panel
          >
            <div
              class="flex flex-col justify-between gap-8 p-9 max-[900px]:gap-7 max-[900px]:p-6"
            >
              <div class="flex justify-between gap-3 text-[#62605e]">
                <span class="eyebrow text-[9px]">
                  0{index + 1} / 0{PROJECTS.length}
                </span>
                <span class="eyebrow text-[9px]">
                  {project.hashtag.includes("personal")
                    ? "Personal project"
                    : "Team project"}
                </span>
              </div>
              <div>
                <h3
                  class="font-heading text-[clamp(48px,5.5vw,80px)] leading-none font-normal max-[900px]:text-5xl"
                  id={`stack-project-${index}`}
                >
                  {project.title}
                </h3>
                <p
                  class="mt-5 max-w-80 text-sm leading-[1.8] text-[#555] max-[900px]:max-w-full"
                >
                  {project.description}
                </p>
                <ul
                  class="mt-6 flex flex-wrap gap-2.5 text-[10px] text-[#666]"
                  aria-label={`${project.title} tags`}
                >
                  {#each project.hashtag as tag (tag)}<li>#{tag}</li>{/each}
                </ul>
              </div>
              {#if project.demoUrl}
                <a
                  class="inline-flex w-37.5 items-center justify-between border-b border-[#999] pb-2 text-[12px]"
                  href={project.demoUrl}
                  target="_blank"
                  rel="external noopener noreferrer"
                >
                  Visit project
                  <ArrowUpRightIcon class="inline-block h-4 w-4" />
                </a>
              {/if}
            </div>
            <div
              class="flex min-w-0 items-center justify-center overflow-hidden bg-[#171719] max-[900px]:row-start-1 max-[900px]:aspect-4/3"
            >
              <img
                class="block h-full w-full object-cover"
                src={project.imgUrl.replace("/project/", "/project-scenes/")}
                alt={`${project.title} on a 14-inch MacBook Pro in a colored studio scene`}
                width="1400"
                height="1050"
                loading="lazy"
              />
            </div>
          </div>
        </article>
      {/each}
    </div>
    <p
      class="mt-14 text-center font-writer text-[22px] leading-[normal] text-[#777] max-[900px]:text-lg"
    >
      That's the stack. More to build.
    </p>
  </div>
</section>
