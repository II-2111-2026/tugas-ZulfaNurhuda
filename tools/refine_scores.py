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
        original_scores = [float(t.get("score", 0)) for t in tests]
        exact_total = sum(original_scores)

        target_total = round(exact_total, 2)

        for t in tests:
            t["score"] = round(float(t.get("score", 0)), 2)

        current_rounded_total = sum(t["score"] for t in tests)
        diff = round(target_total - current_rounded_total, 2)

        if diff != 0:
            for t in reversed(tests):
                if t["score"] > 0:
                    t["score"] = round(t["score"] + diff, 2)
                    break

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
