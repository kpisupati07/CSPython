import sys
import time
from sorts import *
from s7_utils import *

# Test how long sorting takes
def main():
    if (len(sys.argv) != 3):
        print('Usage: python sort_test.py <quick_sort|bubble_sort|insertion_sort|tim_sort> <list size>')
        return
    sort = sys.argv[1]
    N = int(sys.argv[2])

    numbers = random_list(N)
    print("Before:", to_string_truncated(numbers))
    print("Now sorting...")

    start_time = time.time()
    do_sort(sort, numbers)
    elapsed = time.time() - start_time

    print("After:", to_string_truncated(numbers))
    print(f"Took {elapsed:.4f} seconds")

def do_sort(sort_name, numbers):
    if sort_name == "quick_sort":
        quick_sort(numbers)
    elif sort_name == "bubble_sort":
        bubble_sort(numbers)
    elif sort_name == "insertion_sort":
        insertion_sort(numbers)
    elif sort_name == "tim_sort":  # python's built-in sort
        numbers.sort()
    else:
        raise ValueError("Unknown sort function " + sort_name)

if __name__ == "__main__":
    main()
