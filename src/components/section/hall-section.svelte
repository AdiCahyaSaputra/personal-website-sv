<script lang="ts">
  import Dither from "../../$lib/components/svelte-bits/Dither.svelte";
  import ListIcon from "phosphor-svelte/lib/ListIcon";
  import AtIcon from "phosphor-svelte/lib/AtIcon";
  import LinkedinLogoIcon from "phosphor-svelte/lib/LinkedinLogoIcon";
  import GithubLogoIcon from "phosphor-svelte/lib/GithubLogoIcon";
  import TechStackItem from "../reusable/tech-stack-item.svelte";

  const techStacks = [
    { icon: "/assets/tech-stack/django.svg", name: "Django" },
    { icon: "/assets/tech-stack/nestjs.svg", name: "NestJS" },
    { icon: "/assets/tech-stack/nextjs2.svg", name: "Next.js" },
    { icon: "/assets/tech-stack/svelte.svg", name: "Svelte" },
    { icon: "/assets/tech-stack/laravel.svg", name: "Laravel" },
    { icon: "/assets/tech-stack/expo.svg", name: "React Native (Expo)" },
    { icon: "/assets/tech-stack/tanstack.svg", name: "TanStack" },
    { icon: "/assets/tech-stack/python.svg", name: "Python" },
    { icon: "/assets/tech-stack/typescript.svg", name: "TypeScript" },
    { icon: "/assets/tech-stack/go.svg", name: "Golang" },
    { icon: "/assets/tech-stack/trpc.svg", name: "tRPC" },
    { icon: "/assets/tech-stack/pgsql.svg", name: "PostgreSQL" },
    { icon: "/assets/tech-stack/prisma-orm.svg", name: "Prisma ORM" },
    { icon: "/assets/tech-stack/redis.svg", name: "Redis" },
    { icon: "/assets/tech-stack/docker.svg", name: "Docker" },
    { icon: "/assets/tech-stack/git.svg", name: "Git" },
    { icon: "/assets/tech-stack/codex.svg", name: "Codex" },
    { icon: "/assets/tech-stack/figma.svg", name: "Figma" },
    { icon: "/assets/tech-stack/neovim.svg", name: "Neovim" },
    { icon: "/assets/tech-stack/zed.svg", name: "Zed" },
  ];

  const techStackRows = Array.from(
    { length: Math.ceil(techStacks.length / 6) },
    (_, index) => techStacks.slice(index * 6, index * 6 + 6),
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
      class="py-8 md:px-0 px-8 flex justify-between items-center w-full md:w-6xl mx-auto"
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

      <div class="flex flex-col divide-y divide-white/10 select-none">
        {#each techStackRows as row}
          <ul class="flex justify-center divide-x divide-white/10">
            {#each row as stack}
              <TechStackItem icon={stack.icon} name={stack.name} />
            {/each}
          </ul>
        {/each}
      </div>
    </div>
  </div>
</section>
