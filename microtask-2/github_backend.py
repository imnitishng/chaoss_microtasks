
import argparse

from perceval.backends.core.github import GitHub, CATEGORY_ISSUE
import json
import datetime
import dateutil

parser = argparse.ArgumentParser(description="Simple parser for Git commits.")
parser.add_argument("-t", "--token",
                    help = "GitHub token, specify XXX if using Git backend")
parser.add_argument("-r", "--repo",
                    help = "GitHub repository, as 'owner/repo' or gitpath")
parser.add_argument("-d", "--create_dump",
                    help = "y for for creating json dump of data, empty for printing to terminal")

args = parser.parse_args()

from_date = datetime.datetime(2019, 6, 1, 0, 0, 0, tzinfo=dateutil.tz.tzutc())
to_date = datetime.datetime(2020, 2, 1, 0, 0, 0, tzinfo=dateutil.tz.tzutc())

(owner, repo) = args.repo.split('/')
repo = GitHub(owner=owner, repository=repo, api_token=[str(args.token)], sleep_for_rate=True)

issues_gen = repo.fetch(category=CATEGORY_ISSUE, from_date=from_date, to_date=to_date)
issues = list(issues_gen)

if args.create_dump == 'y':
    with open("github_issues.json", "w") as file:
        json.dump(issues, file)
else:
    for issue in issues:
        for field in issue.keys():
            print(str(field) + ':' + str(issue[field]))
        print("-----------")