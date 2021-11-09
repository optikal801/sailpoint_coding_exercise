#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""Query the github repository of your choice to display pull requests for the past N days"""

import argparse 
import datetime
import github

msg = "Query the github repository of your choice to display pull requests for the past N days"
 
# Initializing command-line parser
parser = argparse.ArgumentParser(description = msg)

# Adding optional argument
parser.add_argument("Github_Token", help = "Github Authentication Token (e.g. ghp_HASH)")
parser.add_argument("Github_Repo", help = "Github Repository (e.g. \"repo/repo\")")
parser.add_argument("-d", "--Days", help = "Number of days to list pull requests (e.g. 7). Default is 7 days.", default=7)

github_access_token = parser.parse_args().Github_Token
repository_name = parser.parse_args().Github_Repo 
num_of_days = parser.parse_args().Days 

today = datetime.datetime.today()
date_margin = datetime.timedelta(days = int(num_of_days))

def github_repo(github_access_token, repository_name):
    """Return github repository object"""
    g = github.Github(github_access_token)
    return g.get_repo(repository_name)

def github_fetch_pull_requests(repo):
    """Return github pull requires for passed repository"""
    return repo.get_pulls(sort='created', direction='desc', base='master')

def Pull_Request_Report(github_access_token, repository_name, num_of_days):
    """ Generates a pull request report from the passed repository for the number of days specified"""

    # Instantiate Github class and link to repo
    print(f'Linking to Github repository {repository_name}...')
    repo = github_repo(github_access_token,repository_name)

    # Get paginated list of pull requests for repo
    print(f'Querying Github repository for list of pull requests...')
    all_pull_requests = github_fetch_pull_requests(repo)

    print(f'\nFrom: jeremylfreeman@gmail.com\nTo: devops@sailpoint.com\nSubject: Your GitHub {repository_name} Pull Request Report from the last {num_of_days} days\n\n')
    print(f'There is a total of {all_pull_requests.totalCount} pull requests found in {repository_name} repository, below are the pull requests created in the past {num_of_days} days...\n----------------------------------------------------------------------')
    # Loop through all pull requests
    i = 0
    for pr in all_pull_requests:
        # Instantiate pull request object
        pull_request = repo.get_pull(pr.number)

        if (today - date_margin <= pull_request.created_at <= today + date_margin):
            i += 1
            print(f'\nPull Request #{pull_request.number} - {pull_request.title}\nState: {pull_request.state}\tCreated: {pull_request.created_at}\tUpdated: {pull_request.updated_at}\tCommits: {pull_request.commits}\tComments: {pull_request.comments}\nLink: http://github.com/{repository_name}/pull/{pull_request.number}')
        else:
            break 

    print(f'\n----------------------------------------------------------------------\n\nThere were {i} pull requests for {repository_name} in the past {num_of_days} days\n')

# Execute script
Pull_Request_Report(github_access_token, repository_name, num_of_days)
