# Add your solution to the problem "horoscope" here.


#  Implement a comparison function for dates
#
#  Returns true if the date (month1, day1) is
#  earlier in the calendar than (month2, day2).
#  Assumes the days are valid and doens't do any checking.

def before(month1, day1, month2, day2):  # checks if a day is before the other
    if month1 < month2:
        return True
    elif month1 == month2 and day1 < day2:
        return True
    else:
        return False


# Implement a sign function.
#
# Returns the sign for the given month and day, or
# "INVALID_DATE" if the date is not valid, e.g. month=10 day=54
# Must not print anything out.

def sign(month, day):
    # checks if days are valid by seeing if its within the monts dates and if its not greater than 31 and less than 1
    if (
        month < 1
        or month > 12
        or day < 1
        or day > 31
        or (month == 2 and day > 29)
        or (month == 4 and day > 30)
        or (month == 6 and day > 30)
        or (month == 9 and day > 30)
        or (month == 11 and day > 30)
    ):
        return "INVALID_DATE"
    # checks if its before or after a cetrian date to see if its within the range

    if before(month, day, 4, 20) and not before(month, day, 3, 20):
        return "Aries"
    elif before(month, day, 5, 21) and not before(month, day, 4, 19):
        return "Taurus"
    elif before(month, day, 6, 21) and not before(month, day, 5, 20):
        return "Gemini"
    elif before(month, day, 7, 23) and not before(month, day, 6, 20):
        return "Cancer"
    elif before(month, day, 8, 23) and not before(month, day, 7, 22):
        return "Leo"
    elif before(month, day, 9, 23) and not before(month, day, 8, 22):
        return "Virgo"
    elif before(month, day, 10, 23) and not before(month, day, 9, 22):
        return "Libra"
    elif before(month, day, 11, 22) and not before(month, day, 10, 22):
        return "Scorpio"
    elif before(month, day, 12, 22) and not before(month, day, 11, 21):
        return "Sagittarius"
    elif before(month, day, 2, 19) and not before(month, day, 1, 19):
        return "Aquarius"
    elif before(month, day, 3, 21) and not before(month, day, 2, 18):
        return "Pisces"
    else:
        return "Capricorn"  # this is else because it is december-january so it will be weird if its shown as before, so if everythign else does not work its Capricorn


# Your main function should prompt the user for a month and day and
# print out the sign using return value of the sign function.


def main():
    day = int(input("Whtasf your birthday date: "))
    month = int(input("Whats your birthday month: "))
    if sign(month, day) != "INVALID_DATE":
        print("Your astrological sign is:", sign(month, day))
    else:
        print("INVALID DATE")


# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
