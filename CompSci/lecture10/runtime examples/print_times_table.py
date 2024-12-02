import sys
import time


# PROBLEM: Figure out the order of growth of printing a times
# table of size N by trying various values of N on the command line. 
# If you have time, plot a graph of your results.
def print_times_table(N):
  for i in range(1, N+1):
    for j in range(1, N+1):
      print(f"{i} times {j} is {i*j}")


# Timing code 
def main():
    N = int(sys.argv[1])

    start_time = time.time()
    print_times_table(N)
    elapsed_time = time.time() - start_time

    print(f"Took {elapsed_time:.5f} seconds")


if __name__ == "__main__":
    main()
