# IS6941

from github import Github
import requests

# file path on the repository
file_path = "README.md"

# enter your API token generated from Github
token = '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'
key = Github(token)

# repository format: author/project
repo = key.get_repo("torilee167/IS6941")
file = repo.get_contents(file_path, ref="main")

# decode the content in utf-8
data = file.decoded_content.decode("utf-8")

# write content to a local disk file
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(data)

print("Github data collection completed!")

