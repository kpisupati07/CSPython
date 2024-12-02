# QUESTION: How can we read this extra input from a python program?
#    python args.py some extra data for the program
from sys import argv


def main():
    print(argv)


if __name__ == "__main__":
    main()


