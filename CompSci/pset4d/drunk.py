"""Add your solution to the problem 'drunk' here."""
import random


def drunk_walk():
    """Simulates a random walk. Returns the number blocks walked as well as
    a boolean that is True if ended up at home and False ended up in jail.
    Takes no input parameters. Must not print anything!
    """
    street = 6
    blocks = 0
    while (
        street > 1 and street < 11
    ):  # loops until the street equals home or jail which returns true or false
        direction = random.choice([-1, 1])  # -1 goes back and 1 goes forward
        street += direction
        blocks += 1  # keeps track of how many times it happened
    return (blocks, street == 1)


def main():
    N = 5  # repeats 5 times
    results = []
    for i in range(N):
        print("Here we go again... time for a walk!")
        result = drunk_walk()
        print("Walked", result[0], "blocks, and")
        if result[1] == True:
            print("Landed at HOME")
        else:
            print("Landed in JAIL")
        results.append(result)  # makes a list of all the tuples
    total_blocks = 0
    for x in range(len(results)):
        result = results[x]  # picks each part of the list sepersately gettign tuples
        total_blocks += result[
            0
        ]  # from the tuple it picks the number and adds it to the current amount
    average_blocks = total_blocks / N  # total blocks moves/ number of times moves
    print("Average # of blocks equals", average_blocks)


if __name__ == "__main__":
    main()
