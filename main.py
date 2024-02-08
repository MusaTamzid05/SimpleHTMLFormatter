import argparse
from lib.formatter import FileFormatter


def main():
    parser = argparse.ArgumentParser("html parser")
    parser.add_argument("--path", dest="path", type=str, required=True, help="Path to the target file/dir")
    args = parser.parse_args()
    print(args)

    fl_formatter = FileFormatter(path=args.path)
    fl_formatter.format()


if __name__ == "__main__":
    main()
