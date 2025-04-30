from modules.git_ops import clone_or_pull_repo, checkout_branch
from modules.test_runner import run_pytest
from modules.log_parser import parse_results

# Define repository information
REPO_URL = "https://github.com/wahyeung" 
LOCAL_DIR = "temp_repo"
BRANCH = "master"

def main():
    print("=== Step 1: Git operations ===")
    clone_or_pull_repo(REPO_URL, LOCAL_DIR)
    checkout_branch(LOCAL_DIR, BRANCH)

    print("\n=== Step 2: Run test suite ===")
    log = run_pytest()

    print("\n=== Step 3: Parse test results ===")
    result = parse_results(log)
    print("Test Summary:", result)

if __name__ == "__main__":
    main()