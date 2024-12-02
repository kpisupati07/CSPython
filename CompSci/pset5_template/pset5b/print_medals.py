"""Add your solution to the problem 'print_medals' here."""


def print_medals(medal_counts):
    """Takes the a dictionary of medal counts and prints
    a nicely formatted table with totals for each country
    as described in the pset 5 problem.
    """
    print(f'.               Gold    Silver    Bronze    Total')
    for i in medal_counts:
        print(f'{i:>13}', end="")
        print("     ", medal_counts[i][0], end="")
        print("        ", medal_counts[i][1], end="")
        print("        ", medal_counts[i][2], end="")
        print("       ", medal_counts[i][0] + medal_counts[i][1] + medal_counts[i][2], end="")
        print()






def main():
    # Add your solution to the problem that makes use of the above.
    MEDAL_COUNTS = {
        "Canada": [0, 3, 0],
        "Italy": [0, 0, 1],
        "Germany": [0, 0, 1],
        "Japan": [1, 0, 0],
        "Kazakhstan": [0, 0, 1],
        "Russia": [3, 1, 1],
        "South Korea": [0, 1, 0],
        "United States": [1, 0, 1],
    }
    print(list(MEDAL_COUNTS))
    print_medals(MEDAL_COUNTS)


if __name__ == "__main__":
    main()
