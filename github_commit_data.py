import requests
from datetime import datetime
from dotenv import load_dotenv
import os
from pprint import pprint
import json

load_dotenv()

token = os.environ.get('GITHUB_TOKEN')
username = os.environ.get('GITHUB_USERNAME')


def get_all_repo_names():
    url = f'https://api.github.com/search/repositories?q=user:{username}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code != 200:
        return []
    items = response.json()
    repo_names = [item['name'] for item in items['items']]
    pprint(repo_names)
    print(len(repo_names))
    return repo_names


def get_commits_for_repo(repo_name: str):
    url = f'https://api.github.com/repos/{username}/{repo_name}/commits?per_page=100'
    headers = {'Accept': "application/vnd.github+json",
               'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code != 200:
        return []
    all_commits = response.json()
    user_commits = [commit for commit in all_commits if commit['commit']['committer']['name'] == username]
    clean_commits = [
        {
            'date': commit['commit']['committer']['date'],
            'message': commit['commit']['message'],
        } for commit in user_commits
    ]
    pprint(clean_commits)
    print(len(clean_commits))
    return clean_commits


def get_all_commits():
    data = {}
    repo_names = get_all_repo_names()
    for repo_name in repo_names:
        data[repo_name] = get_commits_for_repo(repo_name)
    pprint(data)
    with open('github_data/github_data_all_commits.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def read_data(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


# Between 19/08/2023 and 26/10/2023
def get_commits_between_dates():
    categorized_commits = read_data('github_data/github_data_all_commits.json')
    all_commits = [commit for repo in categorized_commits.values() for commit in repo]
    commits_by_dates = {}
    for commit in all_commits:
        time = datetime.strptime(commit['date'], '%Y-%m-%dT%H:%M:%SZ')
        if datetime(2023, 8, 19) <= time < datetime(2023, 10, 27):
            date = str(time.date())
            time = str(time.time())
            if date in commits_by_dates:
                commits_by_dates[date].append({
                    'time': time,
                    'message': commit['message'],
                })
            else:
                commits_by_dates[date] = [{
                    'time': time,
                    'message': commit['message'],
                }]
    with open('github_data/github_data_commits_by_date.json', 'w', encoding='utf-8') as f:
        json.dump(commits_by_dates, f, indent=4)


get_commits_between_dates()
