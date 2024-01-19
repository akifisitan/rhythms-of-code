<script lang="ts">
	import CommandMenu from "$lib/components/CommandMenu.svelte";
	import { Button } from "$lib/components/ui/button";
	import { Search, Route } from "lucide-svelte";

	let open = false;
</script>

<nav
	class="sticky z-20 top-0 flex h-16 items-center justify-center gap-0 bg-background/30 shadow-lg backdrop-blur"
>
	<div class="flex justify-center items-center w-96 mx-4">
		<div class="relative flex-grow mx-4 min-w-full">
			<!-- <Search class="absolute left-2.5 top-1/2 transform -translate-y-1/2 h-4 w-4" /> -->
			<Route class="absolute left-2.5 top-1/2 transform -translate-y-1/2 h-4 w-4" />
			<Button
				variant="secondary"
				on:click={() => (open = true)}
				class="bg-slate-800 hover:bg-slate-900 border-slate-400 border-[1px] pl-8 w-full text-slate-400"
				>Navigate <span class="pl-1 text-xs">⌘</span>K
			</Button>
		</div>
	</div>
</nav>

<CommandMenu
	bind:open
	sections={[
		{ url: "#motivation", title: "Motivation" },
		{ url: "#data-collection", title: "Data Collection" },
		{ url: "#data-processing", title: "Data Processing" },
		{ url: "#data-analysis", title: "Data Analysis" },
		{ url: "#conclusion", title: "Conclusion" }
	]}
	links={[
		{
			url: "https://github.com/akifisitan/rhythms-of-code/blob/main/project.ipynb",
			title: "Source Code - Notebook"
		},
		{
			url: "https://github.com/akifisitan/rhythms-of-code/tree/main/scripts",
			title: "Data Collection Scripts"
		},
		{
			url: "https://github.com/akifisitan/rhythms-of-code",
			title: "GitHub Repository"
		}
	]}
/>
