# Add your solution to the problem "fraction_of_day" here.

# Returns the fraction of the day elapsed since midnight.
#
# Must not print anything out.


def fraction_of_day(hour, minute, second, a_p):
    if hour == 12 and minute == 0 and second == 0 and a_p == "A":  # does 12pm
        seconds = 0
    else:
        # make 24 hour so that it can be easily multiplied into seconds
        if a_p == "P":
            hour += 12
        seconds = hour * 3600 + minute * 60 + second
    fraction = seconds / 86400
    return fraction


# Add a main function that prints out a formated table with
# f-strings, as described in the problem set.
def main():
    print("Time        Fraction Since Midnight")  # formats heading
    for i in range(24):  # 24 hours to get both am, and pm
        if i == 0:  # 12am
            hour_12 = 12
            a_p = "A"
        elif i < 12:  # rest of the am
            hour_12 = i
            a_p = "A"
        elif i == 12:  # 12 pm
            hour_12 = i
            a_p = "P"
        else:
            hour_12 = (
                i - 12
            )  # since it goes to 24 it should be -12 to make it back to 12 hour format and aklso make it so that we can see am or pm, rest of the pm
            a_p = "P"
        fraction = fraction_of_day(hour_12, 0, 0, a_p)
        print(f"{hour_12:>2}:00 {a_p}M  {fraction:>8.4f}")


# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
