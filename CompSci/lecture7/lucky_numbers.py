# PROBLEM: keep prompting the user until they guess 1 or 13
# CAUTION! What will happen if you use or?

def main():
    guess = int(input("Please guess a winning number: "))
    while guess != 1 and guess !=13:
            guess = int(input("Please guess a winning number: "))
    print("You got it!")


main()
