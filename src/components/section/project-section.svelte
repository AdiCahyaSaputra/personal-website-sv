<script lang="ts">
  import ProjectCard from "@/components/reusable/project-card.svelte";
  import { PROJECTS } from "@/lib/constants/projects";
</script>

<section class="min-h-screen bg-black px-8 md:px-0 py-8">
  <div class="container mx-auto space-y-4">
    <div
      class="flex justify-between items-stretch border-y border-white/30 w-full"
    >
      <div class="px-4 flex items-center border-x border-white/30">
        <h1 class="text-white md:text-4xl text-xl">
          Projects & Case Study<span class="text-red-600">.</span>
        </h1>
      </div>
      <div class="p-4 border-x border-white/30 max-w-sm">
        <p class="text-white text-base text-justify">
          Production work and earlier builds that show how I approach different
          product problems.
        </p>
      </div>
    </div>

    <div class="flex flex-col gap-4">
      {#each PROJECTS as project, idx}
        <ProjectCard
          title={project.title}
          description={project.description}
          hashtag={project.hashtag}
          imgUrl={project.imgUrl}
          demoUrl={project.demoUrl}
          customClass={project.customClass}
        />
      {/each}
    </div>
  </div>
</section>
