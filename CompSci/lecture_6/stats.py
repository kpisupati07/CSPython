# PROBLEM: Write a function stats that takes two numbers x and y and
# returns their average and absolute difference in a list or a tuple. 

def stats(x, y):
    return [ (x+y/2, abs(x-y))]

def main():
    [average, difference] = stats(10, 26)
    print(average)

if __name__ == "__main__":
    main()
