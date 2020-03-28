
import argparse

from perceval.backends.core.github import GitHub
from perceval.backends.core.git import Git
import json
import datetime
import dateutil

parser = argparse.ArgumentParser(description="Simple parser for Git commits.")
parser.add_argument("-r", "--repo",
                    help = "Git repository URI")
parser.add_argument("-p", "--gitpath",
                    help = "Gitpath of the repository")
parser.add_argument("-d", "--create_dump",
                    help = "y for for creating json dump of data, empty for printing to terminal")

args = parser.parse_args()

from_date = datetime.datetime(2019, 6, 1, 0, 0, 0, tzinfo=dateutil.tz.tzutc())
to_date = datetime.datetime(2020, 1, 1, 0, 0, 0, tzinfo=dateutil.tz.tzutc())

# make sure a cloned repo folder is deleted in gitpath if already present
repo = Git(uri=args.repo, gitpath=args.gitpath)

commits_gen = repo.fetch(from_date=from_date, to_date=to_date)
commits = list(commits_gen)

if args.create_dump == 'y':
    with open("git_commits.json", "w") as file:
        json.dump(commits, file)
else:
    for commit in commits:
        for field in commit.keys():
            print(str(field) + ':' + str(commit[field]))
        print("-----------")