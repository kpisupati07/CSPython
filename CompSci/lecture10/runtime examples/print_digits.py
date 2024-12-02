import sys
import time


# EXAMPLE: Printing digits of a number N is O(log(N)) 
def print_it(N):
    while N > 0:
        print(N % 10)
        N //= 10


def main():
    N = int(sys.argv[1])
    
    start_time = time.time()
    print_it(N)
    elapsed_time = time.time() - start_time
    
    print(f"Took {elapsed_time:.5f} seconds")


if __name__ == "__main__":
    main()
