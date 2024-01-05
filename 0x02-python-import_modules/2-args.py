#!/usr/bin/python3

def main():
    from sys import argv
    argc = len(argv) - 1
    print("{} argument{}{}"
          .format(argc, "" if argc != 1 else "s", ":" if argc > 0 else "."))

    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
