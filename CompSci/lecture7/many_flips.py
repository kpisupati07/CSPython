import random

# PROBLEM: Write a function that keeps flipping a coin until
# we get n heads in a row.
def flip_until_n_heads_in_a_row(n):
    streak = 0
    totalFlips = 0
    while streak != n:
        flip = coin_flip()
        print(flip, end="")
        totalFlips +=1
        if coin_flip() == 'H':
            streak += 1
        else:
            streak = 0
    print(f" Done! It took {totalFlips} flips")

def main():
    num = int(input("How many heads in a row? "))
    flip_until_n_heads_in_a_row(num)

def coin_flip():
    c = random.randint(0,1)
    if c == 0:
        return 'H'
    else:
        return 'T'

if __name__ == "__main__":
    main()

