# Add your solution to the problem "change" here.


# Implement a function print_change that takes in the results of your computation
# and prints them out in a message for the user. For example:
#
# Largest change of 25 from  84  to  59
# occurred between day #6 and day #7.
#
# Must not prompt the user for anything.
def print_change(day1_price, day2_price, day1_num):
    X = abs(
        day2_price - day1_price
    )  # gets difference even if day 1 is > than day 2 bc of the absolute value
    print(
        f"Largest change of {X} from {day1_price} to {day2_price} occurred between day #{day1_num} and day #{day1_num + 1}."
    )


# Implement a function find_change that prompts the user for the
# appropriate number of stock prices and returns a list with the the
# value on the first day, the value on the second day, and the number
# of the first day, in that order.
#
# Takes no parameters.
# Must return a list.
def find_change():
    Past = 0
    Day = 0
    Current = 0
    max_change = 0
    past_current_days = [0, 0, 0]
    for i in range(10):  # goes through all 10 days
        Current = int(input(f"Enter the stock price on day #{i + 1}: "))
        if i > 0:
            change = abs(Current - Past)  # change from previous day to current day
            if change > max_change:
                max_change = change  # updates old with new change which is bigger
                past_current_days = [Past, Current, Day]  # makes list
        Past = Current  # makes the new old as it repeats the loop again
        Day = i + 1
    return past_current_days  # returns the list as the function value

    # Implement a main function that computes the largest change as specified in problem 12,
    # by using find_change to find the largest change and print_change to print the final answer.


def main():
    X = find_change()
    print_change(X[0], X[1], X[2])


# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
