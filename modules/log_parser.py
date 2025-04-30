import re

def parse_results(log_text):
    passed = len(re.findall("PASSED", log_text))
    failed = len(re.findall("FAILED", log_text))
    return {"passed": passed, "failed": failed}