<script lang="ts">
  import ProjectCard from "@/components/reusable/project-card.svelte";
</script>

<section class="h-screen bg-black px-8 md:px-0 py-8">
  <div class="container mx-auto space-y-4">
    <div
      class="flex justify-center items-center border-y border-white/30 w-full"
    >
      <div class="p-4 border-x border-white/30">
        <h1 class="text-white md:text-4xl text-xl">
          Projects & Case Study<span class="text-red-600">.</span>
        </h1>
      </div>
    </div>

    <div>
      <ProjectCard
        title="twillink"
        description="a ugc storefront where brands and creators collaborate and turn social content into a shoppable experience."
        relatedPlace="Crosva"
        imgUrl="/assets/project/twillink.png"
      />
    </div>
  </div>
</section>
