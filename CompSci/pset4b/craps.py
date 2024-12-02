"""Add your solution to the problem 'craps' here."""

import random  # i made this import random because it didnt work before


def do_roll():
    """Simulates rolling 2 dice. Returns the sum of the two rolls."""
    global roll_a  # this is global so that the rolls can be seen everywhere, so that I am able to print the value of the rolls that are rolled
    global roll_b
    roll_a = random.randint(1, 6)  # rolls the dice
    roll_b = random.randint(1, 6)
    return roll_a + roll_b  # returns the sum of the dice


def print_roll(roll_1, roll_2):
    """Prints the results of a roll.
    roll_1, roll_2 are integers representing the rolls.
    Returns nothing.
    """
    print(
        f"Computer rolled a {roll_1} and a {roll_2}, for a total of {roll_1 + roll_2}"
    )  # prints the roll in a good format


def get_point():
    """
    Plays craps (rolls) until a point is established.
    Returns the value of the point.
    """
    roll = do_roll()  # makes roll the sum of the dice
    print_roll(roll_a, roll_b)
    # makes sure that the dice eventually equal 4, 5, 6, 8, 9, 10
    while (
        roll != 4 and roll != 5 and roll != 6 and roll != 8 and roll != 9 and roll != 10
    ):  # and so that it only has to be equal to only one of them before the while loop ends
        roll = do_roll()
        print_roll(
            roll_a, roll_b
        )  # orints progress until dice sum is equal to the desired numbers
    return roll  # returns the sum of the dice, which the point is because it is either 4,5, 6, 8, 9,10


def play_from_point(point):
    """
    Plays using the value of point
    Returns True if the player wins, False otherwise.
    """
    print(f"{point} is now the established POINT.")
    roll = do_roll()  # roll is the sum of the dice
    print_roll(roll_a, roll_b)
    # Check if the sum is equal to the point or to 7
    while roll != point and roll != 7:  # crolls until it is equal to the POINT or 7
        roll = do_roll()
        print_roll(roll_a, roll_b)
    # the following checks if the roll wins or loses
    if roll == point:
        return True
    else:
        return False


def main():
    # rolls until it gets the POINT and then sets point to the value of the POINT
    point = get_point()
    # plays until its POINT or 7 ans sets the return value of true or false as the result
    result = play_from_point(point)
    # if true which is if its the POINT, then you win, otherwise its a 7 which is false which means you ose
    if result:
        print("YOU WIN")
    else:
        print("YOU LOSE")


if __name__ == "__main__":
    main()
