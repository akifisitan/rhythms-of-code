<script>
	import "../app.pcss";
	import Nav from "./Nav.svelte";

	// Highlight.js
	import hljs from "highlight.js/lib/core";
	import "highlight.js/styles/github-dark.css";
	import json from "highlight.js/lib/languages/json";
	import python from "highlight.js/lib/languages/python";
	import { storeHighlightJs } from "$lib/components/codeblock/stores";

	// Register each imported language module
	hljs.registerLanguage("python", python);
	hljs.registerLanguage("json", json);

	storeHighlightJs.set(hljs);
</script>

<Nav />

<slot />
