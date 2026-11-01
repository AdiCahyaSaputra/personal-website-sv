<script lang="ts">
  import { EXPERIENCE } from "$lib/constants/experience";
  import { scrollYears } from "$lib/animations/experience";

  const years = [...new Set(EXPERIENCE.map((role) => role.year))].sort(
    (a, b) => b - a,
  );
  const span = Math.max(...years) - Math.min(...years);
</script>

<section id="experience" aria-label="Experience" class="pb-24">
  <div class="flex flex-col gap-4 p-4 md:p-10" {@attach scrollYears}>
    <h2 class="font-heading text-4xl leading-tight text-[#e5e2dc] md:text-8xl">
      {span} years of experience
    </h2>
    <div data-year-deck class="relative flex flex-col gap-4">
      {#each years as year (year)}
        <article
          data-year-sheet
          class="relative flex min-h-120 w-full max-w-105 flex-col justify-between gap-6 rounded-lg border border-black/15 bg-[#e6e3dc] p-6 text-[#181818] shadow-[-8px_0_24px_#00000012]"
          aria-labelledby={`stack-year-${year}`}
        >
          <h3
            id={`stack-year-${year}`}
            class="font-heading text-7xl leading-none tracking-tight"
          >
            {year}
          </h3>
          <div class="space-y-6">
            {#each EXPERIENCE.filter((role) => role.year === year) as role (role.at)}
              <div>
                <p
                  class="mb-2 text-[10px] tracking-[0.15em] text-black/55 uppercase"
                >
                  {role.type}
                </p>
                <h4 class="text-[22px] leading-tight tracking-tight">
                  {role.experience}
                </h4>
                <p class="mt-2 text-sm leading-relaxed text-black/60">
                  {role.at}
                </p>
              </div>
            {/each}
          </div>
        </article>
      {/each}
    </div>
  </div>
</section>
