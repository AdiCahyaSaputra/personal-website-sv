<script lang="ts">
  import BottomBlur from "@/components/reusable/bottom-blur.svelte";

  import HallSection from "@/components/section/hall-section.svelte";
  import ProjectSection from "@/components/section/project-section.svelte";
</script>

<main class="relative">
  <!-- <BottomBlur /> -->

  <HallSection />

  <div class="relative z-20">
    <ProjectSection />
  </div>
</main>
