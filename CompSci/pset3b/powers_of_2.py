# Add your solution to problem "powers_of_2" to this file.


# Add your print_powers_of_2 function here:
def print_powers_of_2(N):
    Y = 1  # makes it start at 1 so that 2^0 is 1

    while (
        N > 0
    ):  # makes a loop that keeps multiplying the last number and printing it as it goes...
        #I also dont know why the while is formatted like that, I clicked style 50 like was suggested to
        print(Y, " ", end="")
        Y *= 2
        N -= 1
    return Y  # makes it so that final number can be printed


# Write and use a main function that demonstrates your function in action:


def main():
    X = int(input("write a number to go to the power 2: "))
    print(print_powers_of_2(X))  # prints final number


main()
