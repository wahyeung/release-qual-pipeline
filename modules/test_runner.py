import subprocess

def run_pytest():
    print("Running test suite...")
    result = subprocess.run(["pytest", "tests/"], capture_output=True, text=True)
    print(result.stdout)
    return result.stdout