<script lang="ts">
  import { cn } from "cn";
  import { XIcon, ListIcon } from "phosphor-svelte";

  type MenuItem = {
    label: string;
    href: string;
    current?: boolean;
  };

  type Props = {
    items: readonly MenuItem[];
    open?: boolean;
    label?: string;
    ariaLabel?: string;
    class?: string;
  };

  let {
    items,
    open = $bindable(false),
    label = "Menu",
    ariaLabel = "Main navigation",
    class: className = "",
  }: Props = $props();

  const id = $props.id();
  let root: HTMLDivElement;
  let toggle: HTMLButtonElement;
  let linksWidth = $state(0);
  let labelWidth = $state(0);

  function measureLinks(element: HTMLDivElement) {
    const observer = new ResizeObserver(() => {
      linksWidth = element.getBoundingClientRect().width;
    });

    observer.observe(element);

    return () => observer.disconnect();
  }

  function measureLabel(element: HTMLSpanElement) {
    const observer = new ResizeObserver(() => {
      labelWidth = element.getBoundingClientRect().width;
    });

    observer.observe(element);

    return () => observer.disconnect();
  }

  function close() {
    if (root.contains(document.activeElement)) {
      toggle.focus({ preventScroll: true });
    }

    open = false;
  }

  function handlePointerDown(event: PointerEvent) {
    const clickedOutside =
      event.target instanceof Node && !root.contains(event.target);

    if (clickedOutside) open = false;
  }

  function handleFocusIn(event: FocusEvent) {
    const focusedOutside =
      event.target instanceof Node && !root.contains(event.target);

    if (focusedOutside) open = false;
  }

  function handleKeyDown(event: KeyboardEvent) {
    const shouldClose = open && event.key === "Escape";

    if (shouldClose) {
      event.preventDefault();
      close();
    }
  }
</script>

<svelte:document
  onpointerdown={handlePointerDown}
  onfocusin={handleFocusIn}
  onkeydown={handleKeyDown}
/>

<div
  {@attach (element) => {
    root = element;
  }}
  class={[
    "animated-menu group relative inline-block mix-blend-difference rounded-full h-(--size) max-w-full align-middle font-[inherit] text-(length:--menu-font-size,14px) leading-none font-[550] text-(--ink) transition-[width] ease-(--ease) motion-reduce:transition-none! [--size:var(--menu-height,44px)] [--paper:var(--menu-background,#fff)] [--ink:var(--menu-color,#000)] [--ease:cubic-bezier(0.22,1,0.36,1)]",
    open
      ? "w-[calc(var(--links-width)+var(--size))] duration-600"
      : [
          labelWidth > 0
            ? "w-[calc(var(--label-width)+36px+var(--size))]"
            : "w-max",
          "duration-420",
        ],
    className,
  ]}
  data-open={open}
  style:--links-width={`${linksWidth}px`}
  style:--label-width={`${labelWidth}px`}
>
  <span
    class="ml-(--size) h-full px-4.5 grid place-items-center overflow-hidden bg-(--paper) rounded-full transition-opacity duration-140 ease-[ease] group-data-[open=true]:opacity-0 motion-reduce:transition-none!"
    aria-hidden="true"
  >
    <span
      class="block w-max transition-transform duration-300 ease-(--ease) group-data-[open=true]:translate-y-[150%] motion-reduce:transition-none! font-sans"
      {@attach measureLabel}
    >
      <b>Adi</b>cs
    </span>
  </span>

  <button
    {@attach (element) => {
      toggle = element;
    }}
    type="button"
    class="toggle absolute inset-0 cursor-pointer rounded-full border-0 bg-transparent p-0 font-[inherit] text-inherit [-webkit-tap-highlight-color:transparent] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-(--menu-focus-color,currentColor)"
    aria-label={open
      ? `Close ${label.toLowerCase()}`
      : `Open ${label.toLowerCase()}`}
    aria-expanded={open}
    aria-controls={`${id}-links`}
    onclick={() => (open = !open)}
  >
    <span
      class={cn(
        "arrow absolute top-0 left-0 grid size-(--size) place-items-center transition-[left] duration-420 ease-(--ease) group-data-[open=true]:left-[calc(100%-var(--size))] group-data-[open=true]:duration-600 motion-reduce:transition-none! bg-(--paper) rounded-full",
      )}
      aria-hidden="true"
    >
      {#if open}
        <XIcon
          size={20}
          class="transition-transform duration-420 ease-(--ease) group-data-[open=true]:rotate-180 group-data-[open=true]:duration-600 motion-reduce:transition-none!"
        />
      {:else}
        <ListIcon size={20} />
      {/if}
    </span>
  </button>

  <!-- The caller supplies complete URLs, including any SvelteKit base path. -->
  <!-- eslint-disable svelte/no-navigation-without-resolve -->
  <nav
    id={`${id}-links`}
    aria-label={ariaLabel}
    inert={!open}
    class="links-panel invisible absolute inset-y-0 right-(--size) left-0 overflow-hidden overflow-x-auto bg-(--paper) rounded-full opacity-0 scrollbar-none [transition:opacity_160ms_ease,visibility_0s_420ms] group-data-[open=true]:visible group-data-[open=true]:opacity-100 group-data-[open=true]:[transition:opacity_200ms_ease_60ms,visibility_0s] motion-reduce:transition-none! [&::-webkit-scrollbar]:hidden"
  >
    <div
      class="flex h-full w-max box-border items-center px-2.5 [@media(hover:hover)]:[&:has(a:hover)>a:not(:hover)]:opacity-50 [@media(hover:hover)]:[&:has(a:hover)>a]:delay-0"
      {@attach measureLinks}
    >
      {#each items as item, index (`${index}-${item.href}`)}
        <a
          href={item.href}
          aria-current={item.current ? "page" : undefined}
          class="flex min-h-full translate-y-[-110%] items-center justify-center px-2.5 text-inherit no-underline underline-offset-4 whitespace-nowrap opacity-0 [transition:transform_260ms_var(--ease),opacity_130ms_ease] hover:underline focus-visible:rounded-full focus-visible:outline-2 focus-visible:-outline-offset-5 focus-visible:outline-(--ink) aria-[current=page]:underline group-data-[open=true]:translate-y-0 group-data-[open=true]:opacity-100 group-data-[open=true]:delay-[calc(90ms+var(--index)*35ms)] group-data-[open=true]:duration-[480ms,200ms] motion-reduce:transition-none!"
          style:--index={Math.min(index, 6)}
          onclick={close}
        >
          {item.label}
        </a>
      {/each}
    </div>
  </nav>
  <!-- eslint-enable svelte/no-navigation-without-resolve -->
</div>
