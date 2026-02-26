import base64
import json
import os

raw_result = os.environ.get("RAW_RESULT", "")
max_score_str = os.environ.get("MAX_SCORE", "100")

try:
    max_score = float(max_score_str)
except ValueError:
    max_score = 100.0

if not raw_result:
    print("Info: No result to refine")
    exit(0)

try:
    decoded_json = json.loads(base64.b64decode(raw_result).decode("utf-8"))
    tests = decoded_json.get("tests", [])

    if tests:
        original_total = sum(float(t.get("score", 0)) for t in tests)

        for t in tests:
            t["score"] = round(float(t.get("score", 0)), 2)

        new_total = sum(t["score"] for t in tests)

        if abs(original_total - max_score) < 1e-4:
            tests[-1]["score"] = round(tests[-1]["score"] + (max_score - new_total), 2)

        refined_json = json.dumps(decoded_json)
        refined_base64 = base64.b64encode(refined_json.encode("utf-8")).decode("utf-8")

        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"result={refined_base64}\n")
    else:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"result={raw_result}\n")

except Exception as e:
    print(f"Info: Error refining scores: {e}")
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"result={raw_result}\n")
