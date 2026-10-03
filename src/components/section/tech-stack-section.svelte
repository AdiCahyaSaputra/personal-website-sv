<script lang="ts">
  import { TECH_STACKS, type TechStack } from "$lib/constants/skill";
  import TechStackItem from "../reusable/tech-stack-item.svelte";

  const groups = TECH_STACKS.reduce(
    (acc, stack) => {
      if (!acc[stack.group]) {
        acc[stack.group] = [];
      }
      acc[stack.group].push(stack);
      return acc;
    },
    {} as Record<string, TechStack[]>,
  );
</script>

<section
  id="stack"
  class="section shell"
  aria-labelledby="stack-heading"
  tabindex="-1"
>
  <div class="section-intro" data-section-intro>
    <h2 id="stack-heading" class="section-heading">
      My everyday stack<span class="text-red-600">.</span>
    </h2>
    <p class="section-copy">
      The languages, frameworks, and tools I prefer to build with.
    </p>
  </div>
  <div
    class="grid grid-cols-[repeat(2,1fr)] gap-x-16 gap-y-10 mobile:grid-cols-[1fr] mobile:gap-8"
  >
    {#each Object.entries(groups) as [group, stacks] (group)}
      <div class="border-t border-t-line pt-6" data-stack-group>
        <h3 class="eyebrow mb-6 text-[10px] text-muted">{group}</h3>
        <ul class="flex flex-wrap gap-x-7 gap-y-5 mobile:gap-x-6">
          {#each stacks as stack (stack.name)}
            <TechStackItem {...stack} />
          {/each}
        </ul>
      </div>
    {/each}
  </div>
</section>
