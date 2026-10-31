<script lang="ts">
  import { PROJECTS } from "$lib/constants/projects";
  import { stackCards, progressingTitle } from "$lib/animations/project";
</script>

<section id="work" class="bg-black" aria-label="Selected projects">
  <div class="md:px-10 px-4 pt-32 max-[900px]:pt-12">
    <header class="mb-8 flex justify-center gap-8 max-[900px]:mb-8">
      <h2
        class="mt-8 lg:mt-4 font-heading text-4xl md:text-8xl font-bold text-center text-nowrap"
        {@attach progressingTitle}
      >
        Project That I Proud to Showcase
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
            class="flex min-w-0 items-center justify-center overflow-hidden bg-[#171719] w-full aspect-video relative rounded-lg"
            data-card-panel
          >
            <img
              class="block h-full w-full object-cover"
              src={project.imgUrl.replace("/project/", "/project-scenes/")}
              alt={`${project.title} on a 14-inch MacBook Pro in a colored studio scene`}
              width="1400"
              height="1050"
              loading="lazy"
            />

            <div
              class="absolute z-2 top-0 inset-x-0 p-4 flex justify-between items-center bg-linear-to-b from-black/50 to-transparent"
            >
              <h2 class="lg:text-2xl text-lg font-bold font-sans">
                {project.title}
              </h2>
              <ul class="flex">
                {#each project.hashtag as tag (tag)}
                  <li
                    class="py-1 px-2 bg-background text-foreground rounded-full lg:text-sm text-xs font-bold"
                  >
                    {tag}
                  </li>
                {/each}
              </ul>
            </div>
          </div>
        </article>
      {/each}
    </div>
  </div>
</section>
