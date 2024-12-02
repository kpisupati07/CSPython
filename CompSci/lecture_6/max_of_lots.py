# PROBLEM: Write code to read 100 numbers from the  user and report
#          the maximum value back.

def max_of_lots():
    N = 3
    prompt = "Please enter a number: "
    largest = int(input(prompt))

    for i in range(N - 1):
        next = int(input(prompt))
        if (next > largest):
            largest = next


    print("The maximum is", largest)


def main():
    max_of_lots()


if __name__ == "__main__":
    main()
