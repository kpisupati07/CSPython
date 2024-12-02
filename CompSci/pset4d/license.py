"""Add your solution to the problem 'license' here."""
import random


def random_capital():
    """Returns a randomly selected upper-case letter. Takes no input."""

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return random.choice(ALPHABET)  # makes a random letter and returns it


def random_plate():
    """Returns one randomly selected license plate. Takes no input."""
    plate = ""
    plate += str(random.randint(1, 9))  # picks a first random number that is not 0
    plate += str(random.randint(0, 9))
    plate += str(random.randint(0, 9))
    plate += random_capital()
    plate += random_capital()
    plate += random_capital()
    return plate  # returns the whole plate


def main():
    for i in range(20):  # prints the plate 20 times
        print(random_plate())


if __name__ == "__main__":
    main()
