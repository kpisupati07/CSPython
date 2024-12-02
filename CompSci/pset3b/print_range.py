# Add your solution to the problem "print_range" in this file


# Add your print_range function here:
def print_range(x, y):
    if (
        x < y
    ):  # if x is less than y it will count up until they are both equal so that it counts until y
        print(f"[{x}, {y}]: ", end="")
        while x != y:  # runs until x is equal to y
            print(x, ", ", end="", sep="")
            x += 1
        return x
    elif x > y:
        print(f"[{x}, {y}]: ", end="")
        while x != y:  # runs until x is equal to y
            print(x, ", ", end="", sep="")
            x -= 1
        return y
    elif x == y:  # if x=y then print one of them
        print(f"[{x}, {y}]: ", end="")
        return x


# Write and use a main function that demonstrates your function in action:
def main():
    A = int(input("number 1: "))
    B = int(input("number 2: "))
    print(print_range(A, B))  #prints final number from returned function


main()
