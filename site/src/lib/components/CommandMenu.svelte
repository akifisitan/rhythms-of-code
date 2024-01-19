<script lang="ts">
	import * as Command from "$lib/components/ui/command";
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";

	export let sections: { url: string; title: string }[];
	export let links: { url: string; title: string }[];
	export let open = false;

	function down(e: KeyboardEvent) {
		if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
			e.preventDefault();
			open = !open;
		}
	}

	onMount(() => {
		document.addEventListener("keydown", down);
		return () => document.removeEventListener("keydown", down);
	});
</script>

<Command.Dialog bind:open>
	<Command.Input placeholder="Navigate..." />
	<Command.List>
		<Command.Empty>No results found.</Command.Empty>
		<Command.Group heading="Sections">
			{#each sections as { url, title }}
				<Command.Item
					onSelect={() => {
						open = false;
						goto(url);
					}}
				>
					<span>{title}</span>
				</Command.Item>
			{/each}
		</Command.Group>
		<Command.Group heading="Links">
			{#each links as { url, title }}
				<Command.Item
					onSelect={() => {
						open = false;
						window.open(url, "_blank");
					}}
				>
					<span>{title}</span>
				</Command.Item>
			{/each}
		</Command.Group>
		<Command.Separator />
	</Command.List>
</Command.Dialog>
