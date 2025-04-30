from git import Repo
import os

def clone_or_pull_repo(repo_url, local_dir):
    if not os.path.exists(local_dir):
        print(f"Cloning repo into {local_dir}")
        Repo.clone_from(repo_url, local_dir)
    else:
        print(f"Repo already exists. Pulling latest changes.")
        repo = Repo(local_dir)
        repo.remotes.origin.pull()

def checkout_branch(local_dir, branch_name):
    repo = Repo(local_dir)
    repo.git.checkout(branch_name)