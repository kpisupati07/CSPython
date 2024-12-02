# PROBLEM: Move the boolean condition below into a function
# after_july_4th that takes as input the month and the day and returns
# true if the date is after July 4.


def after_fourth(m, d):
    return m > 7 or (m == 7 and d > 4)


def main():
    month = 7
    day = 3
    if after_fourth(m=month, d=day):
        print(f"{month}/{day} is after the fourth")
    else:
        print(f"{month}/{day} is not after the fourth")


if __name__ == "__main__":
    main()
