import argparse
from pathlib import Path


def read_sessions(lines):
    totals = {}
    for line in lines:
        if line.strip():
            minutes, subject = line.split(maxsplit=1)
            subject = subject.strip()
            totals[subject] = totals.get(subject, 0) + int(minutes)
    return totals


def main():
    parser = argparse.ArgumentParser(description="Add up study time by subject.")
    parser.add_argument("log", type=Path, help="text file with one session per line")
    args = parser.parse_args()
    with args.log.open(encoding="utf-8") as log:
        totals = read_sessions(log)

    for subject, minutes in totals.items():
        print(f"{subject}: {minutes} min")
    print(f"Total: {sum(totals.values())} min")


if __name__ == "__main__":
    main()
