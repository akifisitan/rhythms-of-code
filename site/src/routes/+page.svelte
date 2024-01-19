<script lang="ts">
	import CodeBlock from "$lib/components/codeblock/CodeBlock.svelte";
	import TestTable from "./TestTable.svelte";
</script>

<section class="min-h-screen container px-4 sm:px-6 md:px-8 py-8">
	<div class="max-w-3xl mx-auto">
		<main>
			<article class="container prose prose-slate text-slate-400">
				<h1 class="font-extrabold tracking-tight text-slate-200">Rhythms of Code</h1>
				<div class="flex items-center gap-2 text-slate-200 text-sm">
					<img
						class="size-9 my-0 bg-slate-800 rounded-full"
						src="https://avatars.githubusercontent.com/u/102677971?v=4"
						alt="Avatar"
					/>
					<div class="text-sm leading-4">
						<div>Akif Işıtan</div>
						<div class="mt-1">
							<a
								class="text-sky-400 hover:text-sky-600 not-prose"
								target="_blank"
								rel="noopener noreferrer"
								href="https://github.com/akifisitan">@akifisitan</a
							>
						</div>
					</div>
				</div>
				<h2 id="motivation">
					<a href="#motivation" class="text-slate-300 not-prose">Motivation</a>
				</h2>
				<p>
					As a Computer Science student, I wanted to learn about my habits. Writing code
					is more than just an academic activity for me, I like building software in my
					spare time. Over time, I've noticed that music is almost always a part of this
					routine. Whether it's a soothing melody or an upbeat tune, music seems to keep
					me company and possibly, influences my coding efficiency.
				</p>
				<p>
					This got me thinking - does music really make a difference in my productivity?
					This is where this project comes in, I wanted to figure out if there is a
					relation between my sleep, music listening and coding habits.
				</p>
				<h2 id="data-collection">
					<a href="#data-collection" class="text-slate-300 not-prose">Data Collection</a>
				</h2>
				<p>Data collection for the separate entities were listed as follows</p>
				<h3>Collecting daily sleep-wake times</h3>
				<p>
					Obtained this data by writing a script to parse sleep/wake times from my
					personal diary which I keep using <a
						class="text-sky-400 hover:text-sky-500"
						href="https://obsidian.md/"
						target="_blank"
						rel="noopener noreferrer">Obsidian</a
					>. The nice part about Obsidian is that each file is just a markdown file, so
					scraping the necessary part was just a simple script. The full script can be
					seen here. The format is as follows:
				</p>
				<CodeBlock
					language="json"
					code={`{\n\t"2023-08-19": {'sleep': '00:30:00', 'wake': '09:30:00'},\n\t"2023-08-20": {'sleep': '23:00:00', 'wake': '10:30:00'}\n}`}
					twClasses="rounded-lg not-prose"
				/>
				<h3>Collecting Github Contributions</h3>
				<p>
					Obtained daily github commit information using the GitHub API. Since the Github
					API has no direct access to commit information past 180 days, had to come up
					with a work around.
				</p>
				<p>
					First got all the repo names using my access token and stored them as a list,
					then wrote a function to get all the commits for a repository given the
					repository name. Finally, combined these and cleaned up so that the relevant
					dates were collected. A sample output is shown below.
				</p>
				<CodeBlock
					language="json"
					code={`{\n\t"2023-09-17": [\n\t\t{\n\t\t\t'message': 'Update README.md',\n\t\t\t'time':'21:56:03'\n\t\t},\n\t\t{\n\t\t\t'message': 'Handle toasts',\n\t\t\t'time': '11:44:52'\n\t\t}\n\t]\n}`}
					twClasses="rounded-lg not-prose"
				/>
				<h3>Collection Daily Listening Information</h3>
				<p>
					Obtained this data by navigating to <a
						class="text-sky-400 hover:text-sky-500"
						target="_blank"
						rel="noopener noreferrer"
						href="https://www.spotify.com/us/account/privacy/">privacy section</a
					> of my Spotify account and selecting "Extended Streaming History" then requesting
					my data from Spotify. After a week of waiting, the data was ready to use. The data
					was processed and reduced to include relevant dates and songs that were listened
					to for longer than 10 seconds. Sample output data is shown below.
				</p>
				<CodeBlock
					language="json"
					code={`{\n\t'2023-09-23:\n[{\nFeint - Snake Eyes'\n}`}
					twClasses="rounded-lg not-prose"
				/>
				<h2>Data Processing</h2>
				<p>The data was processed and the following dataframe was created:</p>
				<img
					alt="Dataframe Information"
					class="mb-2 rounded-lg"
					src="/images/df_info.png"
				/>
				<p>The dataframe's relevant numeric values can be seen here. A mean just shy of 15 hours of sleep is interesting to know, 2.5 for commits is a bit low and I would like to improve that, and 66 songs per day is maybe a bit excessive </p>
				<img
					alt="Dataframe Described"
					class="mb-2 rounded-lg"
					src="/images/df_describe.png"
				/>
				<p>Dataframe sample:</p>
				<img alt="Dataframe Sample" class="mb-2 rounded-lg" src="/images/df_sample.png" />
				<h2>Data Analysis</h2>
				<p>After obtaining the dataframe, I then plotted some graphs to see the data I am working with and to potentially catch any relations between commits and listening.</p>
				<p>Here's a graph displaying the change of listened minutes per day:</p>
				<img alt="Dataframe Sample" class="mb-2 rounded-lg" src="/images/plots_1.png" />
				<p>And of course, cannot leave commits per day behind:</p>
				<img alt="Dataframe Sample" class="mb-2 rounded-lg" src="/images/plots_2.png" />
				<p>Another interesting graph, the distributions of listened minutes each day depending on the time of day:</p>
				<img alt="Dataframe Sample" class="mb-2 rounded-lg" src="/images/plots_3.png" />
				<p>Again, cannot forget the distributions of commits each day depending on the time of day:</p>
				<img alt="Dataframe Sample" class="mb-2 rounded-lg" src="/images/plots_4.png" />
				<p>And to end this part on a high note, here is a weirdly chaotic but also somehow satisfying graph depicting the change in listened minutes per day in each time of day:</p>
				<img alt="Dataframe Sample" class="mb-2 rounded-lg" src="/images/plots_5.png" />
				<h2>Hypothesis Testing</h2>
				<p>Let's finally test our hypothesis and see if there actually is any correlation between listening to music and coding efficiency.</p>
				<p>First, let's see if there is a correlation between listened minutes and commits:</p>
				<img alt="Dataframe Sample" class="mb-2 rounded-lg" src="/images/plots_6.png" />
				<p>The correlation coefficient is 0.46, which is a moderate correlation. This is a good sign, but let's see if it is statistically significant. Let's use some python magic and see the results:</p>
				<CodeBlock
					language="python"
					code={`from scipy.stats import pearsonr\n\n# Performing Pearson correlation test\ncorrelation_coefficient, p_value = pearsonr(df['total_listened_minutes'], df['total_commit_count'])\n\n\nif p_value < 0.05:\n\tprint(f"Correlation coefficient: {correlation_coefficient:.2f}")\n\tprint("There is a statistically significant correlation between the total listened minutes and the total commit count.")\nelse:\n\tprint("There is no statistically significant correlation between the total listened minutes and the total commit count.")\n\n# Output:\n# p_value: 0.0000845013\n# correlation_coefficient: 0.46\n# There is a statistically significant correlation between the total listened minutes and the total commit count.`}
					twClasses="rounded-lg not-prose"/>
				<p>It seems there is a correlation between the two, let's see if we can fit this data to a linear regression model and see if we can predict the number of commits given the listened minutes:</p>
				<CodeBlock
					language="python"
					twClasses="rounded-lg not-prose"
					code={`from sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error, r2_score\nfrom sklearn.preprocessing import StandardScaler\n\n# Preparing the data\nX = df[['awake_hours', 'total_listened_count', 'total_listened_minutes']]  # Let's use all the available features\ny = df['total_commit_count']  # Target variable\n\n# Splitting the data into training and testing sets\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\nscaler = StandardScaler()\nX_train = scaler.fit_transform(X_train)\nX_test = scaler.transform(X_test)\n\n# Creating the regression model\nmodel = LinearRegression()\n\n# Training the model\nmodel.fit(X_train, y_train)\n\n# Predicting the test set results\ny_pred = model.predict(X_test)\n\n# Evaluating the model\nmse = mean_squared_error(y_test, y_pred)\nr2 = r2_score(y_test, y_pred)\n\nprint(f"Min square error: {mse}")\nprint(f"R2 score: {r2}")\n\n# Output:\n# Min square error: 13.522\n# R2 score: 0.3926`}
				/>
				<p>Not the best result, but it gives us a general idea. I think we got what we wanted, there is a correlation between the two and we can predict the number of commits given the listened minutes.</p>

			</article>
		</main>
	</div>
</section>

<style lang="postcss">
	h2,
	h3 {
		@apply text-slate-300;
	}
</style>
