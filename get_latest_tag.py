import json
import sys


def main(filename: str):
    with open(filename) as f:
        releases = json.load(f)
    versions = [
        # Transform "v0.4.2" -> (0, 4, 2) for sorting
        tuple(map(int, release["tag"].replace("v", "").split(".")))
        for release in releases
    ]
    major, minor, patch = sorted(versions)[-1]
    return f"{major}.{minor}.{patch}"


if __name__ == "__main__":
    print(main(sys.argv[1]))
