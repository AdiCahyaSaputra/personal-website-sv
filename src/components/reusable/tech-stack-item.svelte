<script lang="ts">
  import type { TechStack } from "$lib/constants/skill";
  let { icon, name }: TechStack = $props();
</script>

<li class="flex items-center gap-3 text-[13px] leading-6">
  <img
    src={icon}
    alt=""
    width="21"
    height="21"
    loading="lazy"
    class="size-5.25 object-contain"
  />
  <span>{name}</span>
</li>
