import os
import sys

def parse_scores_from_string(s):
    parts = [p.strip() for p in s.replace(',', ' ').split()]
    scores = []
    for p in parts:
        if p == ":":
            continue
        try:
            scores.append(float(p))
        except ValueError:
            print(f"warning: skipping non-numeric token: {p}")
    return scores

def read_scores():
    if len(sys.argv) > 1:
        return parse_scores_from_string(" ".join(sys.argv[1:]))
    env = os.getenv("SCORES")
    if env:
        return parse_scores_from_string(env)
    if os.path.isfile("scores.txt"):
        with open("scores.txt", "r") as f:
            return parse_scores_from_string(f.read())
    raw = input("Enter scores separated by spaces or commas: ")
    return parse_scores_from_string(raw)

def main():
    scores = read_scores()
    if not scores:
        print("No valid scores provided.")
        sys.exit(1)
    total = sum(scores)
    avg = total / len(scores)

    print("=== main/master branch output ===")
    print(f"Count of scores: {len(scores)}")
    print(f"Sum: {total}")
    print(f"Average: {avg}")
  
