import random
import sys
import time
from searches import *
from s7_utils import *

def do_search(search_name, numbers, value):
    if search_name == "linear_search":
        return linear_search(numbers, value)
    elif search_name == "binary_search":
        return binary_search(numbers, value)
    else:
        raise ValueError("Unknown search function " + search_name)

def main():
    if (len(sys.argv) != 3):
        print('Usage: python search_test.py <linear_search|binary_search> <list size>')
        return
    search_name = sys.argv[1]
    N = int(sys.argv[2])
    numbers = list(range(N)) 
    x = random.randint(0, N-1)
    print(f"Searching for random number {x} in list ",
                      to_string_truncated(numbers))

    start_time = time.time()
    index = do_search(search_name, numbers, x)
    elapsed_time = time.time() - start_time

    print("Found it at", index)
    print(f"Took {elapsed_time:.4f} seconds to search")

if __name__ == "__main__":
    main()
