<script lang="ts">
  import BottomBlur from "@/components/reusable/bottom-blur.svelte";
  import Navbar from "@/components/reusable/navbar.svelte";

  import HallSection from "@/components/section/hall-section.svelte";
  import ProjectSection from "@/components/section/project-section.svelte";
  import ExperienceSection from "@/components/section/experience-section.svelte";
</script>

<main class="relative overflow-x-hidden">
  <Navbar />
  <BottomBlur />

  <HallSection />
  <ProjectSection />
  <ExperienceSection />
</main>
