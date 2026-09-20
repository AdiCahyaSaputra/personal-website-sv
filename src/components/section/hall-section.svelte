<script lang="ts">
  import Dither from "../../$lib/components/svelte-bits/Dither.svelte";
  import ListIcon from "phosphor-svelte/lib/ListIcon";
  import AtIcon from "phosphor-svelte/lib/AtIcon";
  import LinkedinLogoIcon from "phosphor-svelte/lib/LinkedinLogoIcon";
  import GithubLogoIcon from "phosphor-svelte/lib/GithubLogoIcon";
  import TechStackItem from "../reusable/tech-stack-item.svelte";
  import { cx } from "class-variance-authority";
  import { TECH_STACKS } from "../../lib/constants/skill";

  let maxItemPerRow = $state(6);
  let techStackRows = $derived(
    Array.from(
      { length: Math.ceil(TECH_STACKS.length / maxItemPerRow) },
      (_, index) =>
        TECH_STACKS.slice(
          index * maxItemPerRow,
          index * maxItemPerRow + maxItemPerRow,
        ),
    ),
  );
</script>

<section class="bg-black h-screen relative">
  <Dither
    colorNum={8}
    pixelSize={4}
    waveColor={[0.4, 0.4, 0.4]}
    enableMouseInteraction={false}
  />

  <div class="relative z-10 h-screen flex flex-col container mx-auto">
    <nav
      class="py-8 md:px-0 px-8 flex justify-between items-center w-full mx-auto"
    >
      <button class="cursor-target p-2">
        <ListIcon color="white" size={24} />
      </button>

      <ul class="flex items-center md:gap-4 gap-0 group">
        <li class="cursor-target p-2 hover:opacity-100 group-hover:opacity-50">
          <AtIcon size={24} fill="white" weight="fill" />
        </li>
        <li class="cursor-target p-2 hover:opacity-100 group-hover:opacity-50">
          <LinkedinLogoIcon size={24} fill="white" weight="fill" />
        </li>
        <li class="cursor-target p-2 hover:opacity-100 group-hover:opacity-50">
          <GithubLogoIcon size={24} fill="white" weight="fill" />
        </li>
      </ul>
    </nav>

    <div
      class="flex flex-col items-center justify-center text-white h-full gap-5"
    >
      <h1 class="md:text-8xl text-5xl font-bold font-bebas">
        Adi Cahya Saputra<span class="text-red-600">.</span>
      </h1>
      <p class="text-center text-lg font-inter font-light text-white/60">
        Pre-AI Programmer with <b>3 years of</b>
        <br />
        hands-on experience in developing <br />
        <b>full stack web and mobile apps.</b>
      </p>

      <p class="text-white/60">Tech stack/tools I use:</p>

      <div class="flex flex-col divide-y divide-white/30 select-none">
        {#each techStackRows as row, index}
          <ul
            class={cx(
              "flex justify-center divide-x divide-white/30",
              index === techStackRows.length - 1 &&
                "border-x border-white/30 w-max mx-auto",
            )}
          >
            {#each row as stack}
              <TechStackItem icon={stack.icon} name={stack.name} />
            {/each}
          </ul>
        {/each}
      </div>
    </div>
  </div>
</section>
