import oxen
import os
from oxen import LocalRepo
from oxen.remote_repo import create_repo
from oxen import RemoteRepo

# #INITIALIZING LOCAL REPO
# directory = "ChatGPTOxenrepo"
# os.makedirs(directory)

# # Initialize the Oxen Repository
# repo = oxen.init(directory)

#LOAD THE LOCAL REPO and create readme
repo = LocalRepo("ChatGPTOxenrepo")

# filename = os.path.join(repo.path, "README.md")
# with open(filename, "w") as f:
#     f.write("# ChatGPT Bad Answer Prompts\n\n Collection of prompts collected by the community that chatgpt does not answer well.")

# # Add the README.md file to the staging area
# repo.add(filename)
# repo.commit("Adding README.md")

#CREATE REMOTE REPO
remote_name = "nickchu8/ChatGPTBadAnswerPrompt2"
remote_repo = create_repo(remote_name)

#POINT LOCAL TO REMOTE
repo.set_remote("origin", 'https://hub.oxen.ai/nickchu8/ChatGPTBadAnswerPrompt2')

repo.push()

# repo = RemoteRepo()
