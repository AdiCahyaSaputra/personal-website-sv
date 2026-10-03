<script lang="ts">
  import { EXPERIENCE, type Experience } from "$lib/constants/experience";
  import { cn } from "cn";
  const experience = [...EXPERIENCE].reverse().reduce((acc, exp) => {
    acc.push({
      ...exp,
      sameYear: acc.some((r) => r.year === exp.year),
    });

    return acc;
  }, [] as Experience[]);
</script>

<section
  id="experience"
  class="section shell lg:grid lg:grid-cols-[0.85fr_1.5fr] lg:items-start lg:gap-16"
  aria-labelledby="experience-heading"
  tabindex="-1"
>
  <div class="section-intro lg:mb-0 lg:flex-col lg:items-start lg:gap-6" data-experience-intro>
    <h2 id="experience-heading" class="section-heading">
      Experience<span class="text-red-600">.</span>
    </h2>
    <p class="section-copy">
      My path through software development,<br /> starting in 2023.
    </p>
  </div>
  <ol>
    {#each experience as role (`${role.at}-${role.experience}`)}
      <li
        class="grid grid-cols-[1fr_3fr_1fr] items-baseline gap-6 border-t border-t-line py-7.5 mobile:grid-cols-[44px_1fr] mobile:gap-x-5 mobile:gap-y-2.5 mobile:py-6"
        data-experience-row
      >
        <span
          class={cn(
            "text-base text-muted tabular-nums",
            role.sameYear && "opacity-0",
          )}>{role.year}</span
        >
        <div>
          <h3 class="text-[clamp(17px,2vw,23px)] font-[450] tracking-tight">
            {role.experience}
          </h3>
          <p class="mt-2 text-sm leading-[1.7] text-muted">
            {role.at.replace(/^at /, "")}
          </p>
        </div>
        <span
          class="[justify-self:end] text-base text-muted capitalize mobile:col-start-2 mobile:[justify-self:start]"
          >{role.type}</span
        >
      </li>
    {/each}
  </ol>
</section>
