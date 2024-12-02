import random
import sys

filename = sys.argv[1]
n = int(sys.argv[2])

f = open(filename, "w")  # writes
for i in range(n):  # prints n numbers
    f.write(
        str(random.randint(0, 36)) + "\n"
    )  # prints a random number every time, then makes a new line
f.close()
