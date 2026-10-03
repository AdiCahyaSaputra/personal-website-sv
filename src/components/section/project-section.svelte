<script lang="ts">
  import ProjectCard from "../reusable/project-card.svelte";
  import { PROJECTS } from "$lib/constants/projects";
</script>

<section
  id="projects"
  class="section shell"
  aria-labelledby="projects-heading"
  tabindex="-1"
>
  <div class="section-intro" data-reveal>
    <h2 id="projects-heading" class="section-heading">
      Selected work<span class="text-red-600">.</span>
    </h2>
    <p class="section-copy">
      Web and mobile products i was working on with incredible team of engineers
      accross different company.
    </p>
  </div>
  <div class="divide-y divide-line border-t border-t-line">
    {#each PROJECTS as project (project.title)}
      <ProjectCard {project} />
    {/each}
  </div>
</section>
