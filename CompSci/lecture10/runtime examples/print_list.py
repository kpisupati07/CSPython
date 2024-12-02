import random
import sys
import s7_utils
import time


# EXAMPLE: Printing a list is O(N) in the length of the list
def print_list(a):
    for value in a :
        print(value, end=" ")
    print()


# Timing code 
def main():
    N = int(sys.argv[1])
    test = s7_utils.random_list(N)

    start_time = time.time()
    print_list(test)
    elapsed_time = time.time() - start_time

    print(f"Took {elapsed_time:.5f} seconds")


if __name__ == "__main__":
    main()
