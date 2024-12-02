def sum_of_digits(n):
    '''Returns the sum of the digits of n'''
    sum = 0
    while n > 0:
        X = n % 10
        sum += X
        n = n // 10
    return sum



# PROBLEM: Write a function that computes the
# sum of digits of a number n
def main():
    print(sum_of_digits(1298))

if __name__ == "__main__":
    main()
