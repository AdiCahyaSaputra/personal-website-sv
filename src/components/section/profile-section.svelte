<script lang="ts">
  const bio = "I’m a developer based in Jakarta. Since graduating in software engineering in 2023, I’ve been learning by building, working with teams, and solving practical business problems.";
</script>

<section
  class="shell py-14 mobile:grid-cols-[1fr] mobile:gap-5 mobile:py-10"
  aria-label="About me"
  data-profile
>
  <p
    class="max-w-[800px] text-[clamp(18px,2.2vw,28px)] leading-[1.6] tracking-[-0.025em]"
  >
    {#each bio.split(" ") as word, index (index)}
      <span data-bio-word>{word + " "}</span>
    {/each}
  </p>
</section>
