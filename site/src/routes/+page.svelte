<script lang="ts">
	import CodeBlock from "$lib/components/codeblock/CodeBlock.svelte";
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
					This is where this project came in, I wanted to use information I've learned and
					figure out if there is a relation between my sleep, music listening and coding
					habits.
				</p>
				<h2 id="data-collection">
					<a href="#data-collection" class="text-slate-300 not-prose">Data Collection</a>
				</h2>
				<p>
					The data collected can be summarized as sleep and wake times obtained from a
					personal diary, commit information from GitHub to quantify coding efficiency,
					and daily music listening information from Spotify. Keep reading to find out how
					I went over each of them individually.
				</p>
				<h3 class="text-slate-300">Collecting daily sleep-wake times</h3>
				<p>
					Daily sleep-wake data was obtained by writing a script to parse sleep/wake times
					from my personal diary which I keep using <a
						class="text-sky-400 hover:text-sky-500"
						href="https://obsidian.md/"
						target="_blank"
						rel="noopener noreferrer">Obsidian</a
					>. The nice part about Obsidian is that each file is just a markdown file, so
					scraping the necessary part was just a simple script reading from plaintext
					files and parsing them. The full script can be found
					<a
						class="text-sky-400 hover:text-sky-500"
						href="https://github.com/akifisitan/rhythms-of-code/blob/main/scripts/sleep_wake_data.py"
						target="_blank"
						rel="noopener noreferrer">here</a
					>. The end result's format is outlined as follows:
				</p>
				<CodeBlock
					language="json"
					code={`{\n\t"2023-08-19": {'sleep': '00:30:00', 'wake': '09:30:00'},\n\t"2023-08-20": {'sleep': '23:00:00', 'wake': '10:30:00'}\n}`}
					twClasses="rounded-lg not-prose"
				/>
				<h3 class="text-slate-300">Collecting Github Contributions</h3>
				<p>
					Daily GitHub commit data was obtained using the <a
						class="text-sky-400 hover:text-sky-500"
						href="https://docs.github.com/en/rest"
						target="_blank"
						rel="noopener noreferrer">GitHub API</a
					>. The full script can be found
					<a
						class="text-sky-400 hover:text-sky-500"
						href="https://github.com/akifisitan/rhythms-of-code/blob/main/scripts/github_commit_data.py"
						target="_blank"
						rel="noopener noreferrer">here</a
					>, but here is a quick summary of the process:
				</p>
				<p>
					First, I read all the repo names using a personal access token and stored them
					as a list, then wrote a function to get all the commits for a repository given
					the repository name. Finally, combined these and cleaned up so that the relevant
					dates were collected. The end result:
				</p>
				<CodeBlock
					language="json"
					code={`{\n\t"2023-09-17": [\n\t\t{\n\t\t\t'message': 'Update README.md',\n\t\t\t'time':'21:56:03'\n\t\t},\n\t\t{\n\t\t\t'message': 'Handle toasts',\n\t\t\t'time': '11:44:52'\n\t\t}\n\t]\n}`}
					twClasses="rounded-lg not-prose"
				/>
				<h3 class="text-slate-300">Collecting Daily Listening Information</h3>
				<p>
					Obtained this data by navigating to the <a
						class="text-sky-400 hover:text-sky-500"
						target="_blank"
						rel="noopener noreferrer"
						href="https://www.spotify.com/us/account/privacy/">privacy section</a
					>
					of my Spotify account, selecting "Extended Streaming History" and requesting my data
					from Spotify. After a week or so of waiting for the data to be collected, I received
					an email stating that the data was ready to use.
				</p>
				<p>
					I downloaded this data, processed and reduced it to only include relevant dates
					and songs that I listened to for longer than 10 seconds. The full script can be
					found
					<a
						class="text-sky-400 hover:text-sky-500"
						href="https://github.com/akifisitan/rhythms-of-code/blob/main/scripts/spotify_listen_data.py"
						target="_blank"
						rel="noopener noreferrer">here</a
					>. Sample output data is shown below:
				</p>
				<CodeBlock
					language="json"
					code={`{\n\t'2023-08-19': [\n\t\t{\n\t\t\t'name': 'Feint - Snake Eyes',\n\t\t\t'played': '03:10.00',\n\t\t\t'time': '11:39:05'\n\t\t}\n\t]\n}`}
					twClasses="rounded-lg not-prose"
				/>
				<h2 id="data-processing">
					<a href="#data-processing" class="text-slate-300 not-prose">Data Processing</a>
				</h2>
				<p>
					The data was processed, dates were transformed into their necessary datetime
					objects, commits were counted, total listened tracks and minutes were counted.
					The daytimes were broken down and categorized into 4 times of day in morning,
					afternoon, evening and night. In the end, the following dataframe was created:
				</p>
				<img
					alt="Dataframe information described in a table"
					class="mb-2 rounded-lg"
					src="/images/df_info.png"
				/>
				<p>
					Looking at the details of the data on first glance, one interesting takeaway is
					a mean just shy of 15 hours of wake time, good to know. An average of 2.5
					commits per day is a bit low and I would definitely like to improve that.
					Finally, listening to music for 3 hours per day on average is maybe a bit
					excessive, might need to tone that down a bit.
				</p>
				<p>Check the full numeric details of the relevant parts:</p>
				<img
					alt="Dataframe's numeric details described in a table"
					class="mb-2 rounded-lg"
					src="/images/df_describe.png"
				/>
				<p>Here's a random sample from the DataFrame to put things into perspective:</p>
				<img
					alt="Dataframe sample with 7 entries"
					class="mb-2 rounded-lg"
					src="/images/df_sample.png"
				/>
				<h2 id="data-analysis" class="text-slate-300">
					<a href="#data-analysis" class="text-slate-300 not-prose">Data Analysis</a>
				</h2>
				<p>
					After obtaining the dataframe, I then plotted some graphs to see the data I am
					working with and to potentially catch any relations or correlations between
					commits and listening data.
				</p>
				<p>Here's a graph displaying the change in total listened minutes per day:</p>
				<img
					alt="Graph displaying the change in total listened minutes per day"
					class="mb-2 rounded-lg"
					src="/images/plots_1.png"
				/>
				<p>
					And of course, since we're comparing, we cannot leave the change in total
					commits per day behind:
				</p>
				<img
					alt="Graph displaying the change in total commit count per day"
					class="mb-2 rounded-lg"
					src="/images/plots_2.png"
				/>
				<p>
					Another interesting graph regarding listened minutes, displaying the
					distributions of listened minutes each day depending on the time of day:
				</p>
				<img
					alt="Graph displaying the distributions of listened minutes each day depending on the time of day"
					class="mb-2 rounded-lg"
					src="/images/plots_3.png"
				/>
				<p>
					Again, for our goal's sake, we cannot forget the distributions of commits each
					day depending on the time of day:
				</p>
				<img
					alt="Graph displaying distributions of commits each depending depending on the time of day"
					class="mb-2 rounded-lg"
					src="/images/plots_4.png"
				/>
				<p>
					And to end this part on a high note, here is a weirdly chaotic but also somehow
					satisfying graph depicting the change in listened minutes per day in each time
					of day:
				</p>
				<img
					alt="Graph depicting the change in listened minutes per day in each time of day"
					class="mb-2 rounded-lg"
					src="/images/plots_5.png"
				/>
				<h3 class="text-slate-300">Hypothesis Testing</h3>
				<p>
					After visualising some data, it's finally time to test the hypothesis to see if
					there actually is any correlation between listening to music and coding
					efficiency.
				</p>
				<p>
					First, let's compute the correlation matrix of the relevant variables and
					display it as a heatmap to view the degree of correlation between listened
					minutes, commits and awake hours:
				</p>
				<img alt="Dataframe Sample" class="mb-2 rounded-lg" src="/images/plots_6.png" />
				<p>
					It's interesting that there seems to be, although small, negative correlation
					between hours awake and total commit count. This might be due to the fact that I
					tend to sleep less when I have more work to do, which in turn might lead to less
					commits. This is just a hypothesis, but it's interesting to see that there is at
					least some degree of correlation between the two. I'm more interested in the
					relationship between listened minutes and commits, so let's take a look at that:
				</p>
				<p>
					The correlation coefficient between our two variables was calculated to be 0.46,
					which is a moderate correlation. This is a good sign, let's see if this is
					statistically significant by using some python magic:
				</p>
				<CodeBlock
					language="python"
					code={`from scipy.stats import pearsonr\n\n# Performing Pearson correlation test\ncorrelation_coefficient, p_value = pearsonr(df['total_listened_minutes'], df['total_commit_count'])\n\n\nif p_value < 0.05:\n\tprint(f"Correlation coefficient: {correlation_coefficient:.2f}")\n\tprint("There is a statistically significant correlation between the total listened minutes and the total commit count.")\nelse:\n\tprint("There is no statistically significant correlation between the total listened minutes and the total commit count.")\n\n# Output:\n# p_value: 0.0000845013\n# correlation_coefficient: 0.46\n# There is a statistically significant correlation between the total listened minutes and the total commit count.`}
					twClasses="rounded-lg not-prose"
				/>
				<p>
					It seems there is considerable positive correlation between the two, seems our
					hypothesis was not too bad. Now that we have the boring hypothesis testing
					section over and done with, let's have some fun.
				</p>
				<h3 class="text-slate-300">Machine Learning</h3>
				<p>
					Although we have a very small dataset, let's see if we can fit this data to a
					linear regression model and test how well it performs and if we can predict the
					number of commits given the listened minutes accurately:
				</p>
				<CodeBlock
					language="python"
					twClasses="rounded-lg not-prose"
					code={`from sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error, r2_score\nfrom sklearn.preprocessing import StandardScaler\n\n# Preparing the data\nX = df[['awake_hours', 'total_listened_count', 'total_listened_minutes']]  # Let's use all the available features\ny = df['total_commit_count']  # Target variable\n\n# Splitting the data into training and testing sets\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\nscaler = StandardScaler()\nX_train = scaler.fit_transform(X_train)\nX_test = scaler.transform(X_test)\n\n# Creating the regression model\nmodel = LinearRegression()\n\n# Training the model\nmodel.fit(X_train, y_train)\n\n# Predicting the test set results\ny_pred = model.predict(X_test)\n\n# Evaluating the model\nmse = mean_squared_error(y_test, y_pred)\nr2 = r2_score(y_test, y_pred)\n\nprint(f"Min square error: {mse}")\nprint(f"R2 score: {r2}")\n\n# Output:\n# Min square error: 13.522\n# R2 score: 0.3926`}
				/>
				<p>
					The result is not that great, but it gives us a general idea. Maybe in a future
					project I will have more data to test around with and we can then really see,
					trying different models does not really make sense in this regard. I think for
					the most part, I got what wanted.
				</p>
				<h2 id="conclusion">
					<a href="#conclusion" class="text-slate-300 not-prose">Conclusion</a>
				</h2>
				<p>
					This project has been a great journey for me. Taking a look into my own data,
					thinking about kinds of questions I could come up with regarding the data and
					finally, trying to answer those questions has been a great learning experience.
					I discovered an interesting link, the more I listened to music, the more commits
					I tended to make. It's a curious thing, especially since coding is not just
					about committing. Often, there's a lot of unseen work behind each commit.
					Despite this, the pattern that emerged was intriguing and spoke volumes about
					how music might be influencing my coding rhythm.
				</p>
				<p>
					However, I must acknowledge that my study had its limitations. With only 69 data
					points, I'm just scratching the surface. In future projects, I plan to gather
					more data, commit more often, and maybe even explore how my typing speed plays
					into all this. Who knows what other insights are waiting to be uncovered?
				</p>
				<p>
					Thank you very much for reading, I hope you enjoyed taking part in this project
					as much as I did. Have a great one.
				</p>
				<p>- Akif</p>
			</article>
		</main>
	</div>
</section>
