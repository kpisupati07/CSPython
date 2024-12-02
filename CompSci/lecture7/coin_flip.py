import random

# PROBLEM: Mwrite a function that simulates a
# coin flip and returns 'H' or 'T' with equal
# probablity
def coin_flip():
    c = random.randint(0,1)
    if c == 0:
        return 'H'
    else:
        return 'T'



def main():
    c = coin_flip()
    print("You flipped " + c)
    if c == 'H':
        print("I win!")
    else:
        print("You win!")

if __name__ == "__main__":
    main()
