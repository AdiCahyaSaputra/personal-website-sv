<script lang="ts">
  import ScrollReveal from "@/$lib/components/svelte-bits/ScrollReveal.svelte";
</script>

<section class="h-[60vh] bg-black md:px-0 px-8 py-24">
  <div
    class="container mx-auto h-max text-white lg:max-w-6xl"
    data-scroll
    data-scroll-speed="0.2"
  >
    <ScrollReveal
      text="I live in Jakarta, Indonesia... Graduated from vocational high school in
      2023 majoring in Software Engineering. Since then, I&apos;ve been learning
      by building and working with teams to solve practical business problems.
      Here is the problems..."
      textClassName="text-7xl font-bold font-heading text-center"
      baseRotation={0}
      enableBlur={false}
    />
  </div>
</section>
