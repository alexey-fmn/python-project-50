import argparse

from gendiff.extension_selector import extension_selector


def main():
    parser = argparse.ArgumentParser(description="Compare two files "
                                                 "and show difference")
    parser.add_argument("file1")
    parser.add_argument("file2")
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        choices=['stylish', 'plain'],
        help='set format of output'
    )

    args = parser.parse_args()

    return extension_selector(args.file1, args.file2, args.format)


if __name__ == "__main__":
    main()