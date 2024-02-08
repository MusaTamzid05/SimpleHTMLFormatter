import argparse
from lib.formatter import FileFormatter
from lib.formatter import DirFormatter
import os


def main():
    parser = argparse.ArgumentParser("html parser")
    parser.add_argument("--path", dest="path", type=str, required=True, help="Path to the target file/dir")
    args = parser.parse_args()

    formatter = None

    if os.path.isdir(args.path):
        formatter = DirFormatter(path=args.path)
    else:
        formatter = FileFormatter(path=args.path)

    formatter.format()


if __name__ == "__main__":
    main()
