<script lang="ts">
  import ArrowUpRightIcon from "phosphor-svelte/lib/ArrowUpRightIcon";
  import { CONTACTS } from "$lib/constants/contact";
  let { compact = false } = $props<{ compact?: boolean }>();
</script>

<ul class={compact ? "flex flex-wrap gap-6" : "grid grid-cols-[repeat(3,1fr)] gap-8 mobile:grid-cols-[1fr] mobile:gap-0"}>
  {#each CONTACTS as contact (contact.label)}
    <li class="min-w-0">
      {#if contact.href}
        <a
          class={["flex flex-wrap items-center justify-between gap-3 transition-[color] duration-200 ease-[ease] hover:text-accent", compact ? "border-0 py-2 text-[13px]" : "border-t border-t-line py-6 text-[20px]"]}
          href={contact.href}
          target={contact.href.startsWith("mailto:") ? undefined : "_blank"}
          rel={contact.href.startsWith("mailto:")
            ? undefined
            : "noopener noreferrer"}
        >
          <span>{contact.label}</span>
          <ArrowUpRightIcon size={20} />
        </a>
      {:else}
        <div class={["flex flex-wrap justify-between", compact ? "flex-col [align-items:start] gap-1 border-0 py-2 text-[13px]" : "items-center gap-3 border-t border-t-line py-6 text-[20px]"]}>
          <span>{contact.label}</span>
          <span class={["text-muted", compact ? "text-[10px]" : "text-[11px]"]}>{contact.pendingLabel}</span>
        </div>
      {/if}
    </li>
  {/each}
</ul>
