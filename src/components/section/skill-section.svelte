<script>
  import { TECH_STACKS } from "$lib/constants/skill";
  import EncryptedText from "../reusable/encrypted-text.svelte";

  const groupStyles = new Map([
    [
      "Languages & Backend",
      "border-amber-300/40 bg-amber-300/10 text-amber-200",
    ],
    ["Web & Mobile", "border-sky-300/40 bg-sky-300/10 text-sky-200"],
    [
      "Data & Infrastructure",
      "border-emerald-300/40 bg-emerald-300/10 text-emerald-200",
    ],
    ["Tools", "border-violet-300/40 bg-violet-300/10 text-violet-200"],
  ]);

  const symbols = new Map([
    ["Django", "Dj"],
    ["NestJS", "Nj"],
    ["Next.js", "Nx"],
    ["Svelte", "Sv"],
    ["Laravel", "Lv"],
    ["React Native (Expo)", "Ex"],
    ["TanStack", "Tn"],
    ["Python", "Py"],
    ["TypeScript", "Ts"],
    ["Golang", "Go"],
    ["tRPC", "Tr"],
    ["PostgreSQL", "Pg"],
    ["Prisma ORM", "Pr"],
    ["Redis", "Rd"],
    ["Docker", "Dk"],
    ["Git", "Gt"],
    ["Codex", "Cx"],
    ["Figma", "Fg"],
    ["Neovim", "Nv"],
    ["Zed", "Zd"],
  ]);

  const groups = [...new Set(TECH_STACKS.map((skill) => skill.group))];
</script>

<section id="stack" class="mt-32 p-4 md:p-10">
  <div class="flex justify-between items-start">
    <h1 class="text-4xl text-left md:text-8xl font-heading">
      The <br /> Stack &amp; <br /> Tools
    </h1>
    <h1 class="text-4xl text-right md:text-8xl font-heading">
      Used to <br />
      <EncryptedText
        texts={["Design", "Develop", "Deploy"]}
        class="uppercase"
      /><br />the app
    </h1>
  </div>

  <ul
    class="mt-8 grid w-full list-none grid-cols-3 gap-2 p-0 sm:grid-cols-4 sm:gap-3 lg:grid-cols-8"
    aria-label="Periodic table of my skills"
  >
    {#each TECH_STACKS as skill, index (skill.name)}
      <li
        class="grid aspect-square min-w-0 grid-rows-[auto_1fr_auto] rounded-sm border p-2 sm:p-3 lg:nth-[2]:col-start-8 lg:nth-[5]:col-start-5 lg:nth-[17]:col-start-3 {index >=
        16
          ? 'lg:mt-4'
          : ''} {groupStyles.get(skill.group)}"
        aria-label={`${skill.name}, ${skill.group}`}
      >
        <div class="flex items-center justify-between gap-2" aria-hidden="true">
          <span class="text-[10px] leading-none tabular-nums sm:text-xs">
            {String(index + 1).padStart(2, "0")}
          </span>
          <img
            src={skill.icon}
            alt=""
            class="size-4 shrink-0 object-contain sm:size-5"
            loading="lazy"
          />
        </div>
        <span
          class="self-center text-center text-3xl font-medium tracking-tight sm:text-4xl xl:text-5xl"
          aria-hidden="true"
        >
          {symbols.get(skill.name)}
        </span>
        <span
          class="text-center text-[10px] leading-tight text-balance sm:text-xs"
        >
          {skill.name}
        </span>
      </li>
    {/each}
  </ul>

  <ul
    class="mt-8 flex w-full list-none flex-wrap justify-start md:justify-center gap-x-6 gap-y-3 p-0 sm:mt-10 sm:gap-x-8"
    aria-label="Skill group legend"
  >
    {#each groups as group (group)}
      <li class="flex items-center gap-2 text-xs text-zinc-300 sm:text-sm">
        <span
          class="size-3 shrink-0 rounded-xs border {groupStyles.get(group)}"
          aria-hidden="true"
        ></span>
        {group}
      </li>
    {/each}
  </ul>
</section>
