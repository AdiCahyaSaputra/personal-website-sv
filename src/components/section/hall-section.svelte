<script lang="ts">
	import { AtIcon, GithubLogoIcon, LinkedinLogoIcon } from "phosphor-svelte";
	import { CONTACTS } from "$lib/constants/contact";
	import EncryptedText from "../reusable/encrypted-text.svelte";
</script>

<section
	class="w-full h-screen bg-black p-4 md:p-10 flex justify-center items-center"
>
	<div
		class="bg-background w-full h-full rounded-lg flex flex-col justify-center items-center gap-8 relative"
	>
		<h1
			class="text-center font-writer text-5xl leading-[1.08] font-bold md:text-8xl text-foreground"
		>
			Agnostic
			<br />
			<EncryptedText
				texts={["Framework", "Platform", "AI Tools"]}
				interval={3000}
			/>
			<br />
			Programmer
		</h1>

		<div class="flex flex-col gap-2 w-full items-center">
			<p
				class="text-foreground/60 md:text-xl text-sm max-w-1/2 md:w-full text-center"
			>
				Building software since AI were still stupid
			</p>

			<!-- Contact -->
			<div
				class="flex items-center [@media(hover:hover)]:[&:has(a:hover)>a:not(:hover)]:opacity-50"
			>
				{#each CONTACTS as contact (contact.label)}
					{#if contact.href}
						<a
							href={contact.href}
							aria-label={contact.label}
							title={contact.label}
							target="_blank"
							rel="external noopener"
							class="inline-flex size-11 items-center justify-center rounded-full text-foreground transition-opacity duration-200 motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-foreground"
						>
							{#if contact.label === "GitHub"}
								<GithubLogoIcon weight="fill" size={28} aria-hidden="true" />
							{:else if contact.label === "LinkedIn"}
								<LinkedinLogoIcon weight="fill" size={28} aria-hidden="true" />
							{:else if contact.label === "Email"}
								<AtIcon weight="fill" size={28} aria-hidden="true" />
							{/if}
						</a>
					{/if}
				{/each}
			</div>
		</div>

		<img
			src="/assets/avatar/adics-head.png"
			alt="Adi looking up at the technologies"
			class="pointer-events-none absolute bottom-0 left-1/2 -translate-x-1/2 z-1 w-[min(50vw,640px)] max-md:w-[min(100%,640px)]"
		/>
	</div>
</section>
