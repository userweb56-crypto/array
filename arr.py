import sys

def parse(s):
    nums = []
    for x in s.replace(",", " ").split():
        try:
            nums.append(float(x))
        except ValueError:
            print(f"warning: skipping non-numeric token: {x}")
    return nums

def read_scores():
    # Use command-line arguments if provided
    if len(sys.argv) > 1:
        return parse(" ".join(sys.argv[1:]))

    # Otherwise, always ask for terminal input
    return parse(input("Enter scores separated by spaces or commas: "))

def main():
    scores = read_scores()

    if not scores:
        print("No valid scores provided.")
        sys.exit(1)

    print("=== Output ===")
    print(f"Count of scores: {len(scores)}")
    print(f"Sum: {sum(scores)}")
    print(f"Average: {sum(scores) / len(scores)}")
    print(f"Maximum: {max(scores)}")
    print(f"Minimum: {min(scores)}")

if __name__ == "__main__":
    main()