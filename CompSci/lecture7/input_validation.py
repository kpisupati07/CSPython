# PROBLEM: Keep prompting the user if they enter a negative age
def main():
    age = int(input("Please enter an age in years: "))
    while age < 0:
        age = int(input("Please enter a positive age: "))

    print("Thank you for entering", age)
if __name__ == "__main__":
    main()
