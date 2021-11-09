usage: github_pull_requests_report.py [-h] [-d DAYS] Github_Token Github_Repo

Query the github repository of your choice to display pull requests for the past N days

positional arguments:
  Github_Token          Github Authentication Token (e.g. ghp_HASH)
  Github_Repo           Github Repository (e.g. "repo/repo")

optional arguments:
  -h, --help            show this help message and exit
  -d DAYS, --Days DAYS  Number of days to list pull requests (e.g. 7). Default is 7 days.

