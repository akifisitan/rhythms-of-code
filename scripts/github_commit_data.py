import requests
from datetime import datetime
import os
from pprint import pprint
from dotenv import load_dotenv
from utils import write_data

# Load environment variables from .env file
load_dotenv()

token = os.environ.get('GITHUB_TOKEN')
username = os.environ.get('GITHUB_USERNAME')

# Get all repository names including private ones using personal access token
def get_all_repo_names():
    url = f'https://api.github.com/search/repositories?q=user:{username}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching repository names, code: {response.status_code}")
        return []
    items = response.json()
    repo_names = [item['name'] for item in items['items']]
    return repo_names

# Get all commits for a repository
def get_commits_for_repo(repo_name: str):
    url = f'https://api.github.com/repos/{username}/{repo_name}/commits?per_page=100'
    headers = {'Accept': "application/vnd.github+json",
               'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching commits, code: {response.status_code}")
        return []
    all_commits = response.json()
    user_commits = [commit for commit in all_commits if commit['commit']['committer']['name'] == username]
    clean_commits = [
        {
            'date': commit['commit']['committer']['date'],
            'message': commit['commit']['message'],
        } for commit in user_commits
    ]
    return clean_commits

# Combine and filter commits by date
def collect_commits_between_dates():
    data = {}
    repo_names = get_all_repo_names()
    print(f"Repository Count: {len(repo_names)}")
    for repo_name in repo_names:
        data[repo_name] = get_commits_for_repo(repo_name)
    all_commits = [commit for repo in data.values() for commit in repo]
    commits_by_date = {}
    for commit in all_commits:
        time = datetime.strptime(commit['date'], '%Y-%m-%dT%H:%M:%SZ')
        if datetime(2023, 8, 19) <= time < datetime(2023, 10, 27):
            date = str(time.date())
            time = str(time.time())
            if date in commits_by_date:
                commits_by_date[date].append({
                    'time': time,
                    'message': commit['message'],
                })
            else:
                commits_by_date[date] = [{
                    'time': time,
                    'message': commit['message'],
                }]
    return commits_by_date


commits_by_dates = collect_commits_between_dates()
pprint(commits_by_dates["2023-09-17"])

# Store the data in a json file for processing later
write_data("data_commits_by_date.json", commits_by_dates)
