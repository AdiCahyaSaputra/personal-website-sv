<script lang="ts">
  import ArrowUpRightIcon from "phosphor-svelte/lib/ArrowUpRightIcon";
  import type { Project } from "$lib/constants/projects";
  import FillLink from "./fill-link.svelte";
  let { project }: { project: Project } = $props();
</script>

<article
  class="grid grid-cols-[0.85fr_1.5fr] items-center gap-16 py-12 mobile:grid-cols-[1fr] mobile:gap-7 mobile:py-8"
  data-project
>
  <div class="py-3 mobile:p-0" data-project-copy>
    <div class="eyebrow flex gap-3.5 text-[9px] text-muted">
      {#each project.hashtag as tag (tag)}<span>{tag}</span>{/each}
    </div>
    <h3
      class="mt-7 font-heading text-[clamp(3rem,5vw,4.5rem)] leading-none mobile:mt-4"
    >
      {project.title}
    </h3>
    <p
      class="mt-5 max-w-[330px] text-[14px] leading-[1.85] text-muted mobile:mt-3.5 mobile:max-w-none"
    >
      {project.description}
    </p>
    {#if project.demoUrl}
      <FillLink
        class="mt-7 mobile:mt-[18px]"
        href={project.demoUrl}
        target="_blank"
        rel="noopener noreferrer"
        aria-label={`Visit ${project.title} (opens in a new tab)`}
        >Visit website <ArrowUpRightIcon size={18} /></FillLink
      >
    {/if}
  </div>
  <div
    class="overflow-hidden bg-surface p-[clamp(20px,3.5vw,48px)] mobile:row-start-1 mobile:p-6"
    data-project-image
  >
    <img
      class="block h-auto w-full"
      src={project.imgUrl}
      alt={`${project.title} website preview`}
      width="1600"
      height="942"
      loading="lazy"
      decoding="async"
    />
  </div>
</article>
