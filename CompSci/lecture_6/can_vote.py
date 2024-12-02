# PROBLEM: Write a function can_vote that takes an age and returns
# True if the person is old enough to vote.

def can_vote(a):
    return (a>=18)

def main():
    age = int(input("Please enter your age: "))
    if (can_vote(age)):
        print("Here's your ballot!")
    else:
        print("Sorry!")


if __name__ == "__main__":
    main()
