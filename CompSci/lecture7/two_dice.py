import random

# PROBLEM: Extend this program to roll two dice
# using randint until they match
def main():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print(f"Rolled a {roll1} and a {roll2}")
    while roll1 != roll2:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print(f"Rolled a {roll1} and a {roll2}")

if __name__ == "__main__":
    main()
