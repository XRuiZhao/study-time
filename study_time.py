import argparse
from pathlib import Path


def read_sessions(lines):
    totals = {}
    for number, line in enumerate(lines, start=1):
        fields = line.strip().split(maxsplit=1)
        if not fields:
            continue
        if len(fields) == 1:
            raise ValueError(f"line {number}: use minutes followed by a subject")
        minutes, subject = fields
        if not minutes.isdecimal() or int(minutes) == 0:
            raise ValueError(f"line {number}: minutes must be a positive whole number")
        totals[subject] = totals.get(subject, 0) + int(minutes)
    return totals


def main():
    parser = argparse.ArgumentParser(description="Add up study time by subject.")
    parser.add_argument("log", type=Path, help="text file with one session per line")
    args = parser.parse_args()
    try:
        with args.log.open(encoding="utf-8") as log:
            totals = read_sessions(log)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{args.log}: {error}\n")

    for subject, minutes in totals.items():
        print(f"{subject}: {minutes} min")
    print(f"Total: {sum(totals.values())} min")


if __name__ == "__main__":
    main()
