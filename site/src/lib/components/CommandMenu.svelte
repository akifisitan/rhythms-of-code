<script lang="ts">
	import * as Command from "$lib/components/ui/command";
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";

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
	<Command.Input placeholder="Navigate to a section..." />
	<Command.List>
		<Command.Empty>No results found.</Command.Empty>
		<Command.Group heading="Sections">
			{#each links as { url, title }}
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
		<Command.Separator />
	</Command.List>
</Command.Dialog>
