import argparse

from gendiff.diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Compare two files and show difference")
    parser.add_argument("file1")
    parser.add_argument("file2")
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    return generate_diff(args.file1, args.file2)

if __name__ == "__main__":
    main()