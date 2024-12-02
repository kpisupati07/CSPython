import random

# PROBLEM: Print random numbers from 1 to 100 until you get one over 90
def main():
     X = (random.randint(1, 100))
     print(X, end=' ')
     while X <= 90:
          X = (random.randint(1, 100))
          print(X, end=' ')
     print()

if __name__ == "__main__":
    main()
