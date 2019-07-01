#!/usr/bin/python3

from git import Repo
import git

def git_push():
    PATH_TO_GIT_REPO = "."
    COMMENTS = "committing repo"

    repo = Repo(PATH_TO_GIT_REPO)
    repo.git.add([PATH_TO_GIT_REPO +'/*'])  
    repo.index.commit(COMMENTS)
    origin = repo.remote("origin")
    origin.push()

git_push()
