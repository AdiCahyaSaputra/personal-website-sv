<script lang="ts">
  import ProjectCard from "@/components/reusable/project-card.svelte";
  import { PROJECTS } from "@/lib/constants/projects";
  import { onMount } from "svelte";
  import { gsap } from "gsap";
  import { ScrollTrigger } from "gsap/ScrollTrigger";
  import { cn } from "cn";

  gsap.registerPlugin(ScrollTrigger);

  let sectionElement: HTMLElement;
  let cardsElement: HTMLDivElement;

  onMount(() => {
    const context = gsap.context(() => {
      const media = gsap.matchMedia();

      media.add(
        "(min-width: 768px) and (prefers-reduced-motion: no-preference)",
        () => {
          const cardWrappers = Array.from(
            cardsElement.querySelectorAll<HTMLElement>("[data-project-card]"),
          );

          cardWrappers.forEach((wrapper, index) => {
            const card = wrapper.firstElementChild;
            const isLastCard = index === cardWrappers.length - 1;

            if (!(card instanceof HTMLElement)) return;

            gsap.to(card, {
              // scale: isLastCard ? 1 : 0.98 + index * 0.01,
              transformOrigin: "top center",
              ease: "none",
              scrollTrigger: {
                trigger: wrapper,
                start: "top top",
                endTrigger: cardsElement,
                end: "bottom center",
                scrub: true,
                pin: wrapper,
                pinSpacing: false,
                invalidateOnRefresh: true,
              },
            });
          });
        },
      );

      return () => media.revert();
    }, sectionElement);

    return () => context.revert();
  });
</script>

<section bind:this={sectionElement} class="min-h-screen bg-black py-8">
  <div class="space-y-4 relative">
    <div
      class="container mx-auto px-8 md:px-0 flex flex-col md:flex-row md:justify-between md:items-center rounded-sm w-full"
    >
      <div class="flex items-center">
        <h1 class="text-white md:text-4xl text-2xl">
          Projects & Case Study<span class="text-red-600">.</span>
        </h1>
      </div>
      <div class="max-w-xs">
        <p class="text-white text-base text-justify">
          Production work and earlier builds that show how I approach different
          product problems.
        </p>
      </div>
    </div>

    <div
      bind:this={cardsElement}
      class="flex flex-col bg-black md:bg-transparent relative md:static z-10"
    >
      {#each PROJECTS as project, index}
        <div
          data-project-card
          class={cn("w-full perspective-normal", index > 0 && "md:-mt-16")}
        >
          <ProjectCard
            title={project.title}
            description={project.description}
            hashtag={project.hashtag}
            imgUrl={project.imgUrl}
            demoUrl={project.demoUrl}
            customClass={project.customClass}
          />
        </div>
      {/each}
    </div>
  </div>
</section>
