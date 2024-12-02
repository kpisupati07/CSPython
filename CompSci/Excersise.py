# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself
# To find the prime numbers from 1 to 100, we can use a loop and check each number for divisibility
# We can use a flag variable to indicate whether a number is prime or not

# Loop from 1 to 100
for num in range(1, 101):
    # Assume the number is prime
    is_prime = True
    # Loop from 2 to the square root of the number
    for factor in range(2, int(num**0.5) + 1):
        # If the number is divisible by any factor, it is not prime
        if num % factor == 0:
            is_prime = False
            # No need to check further factors, so set factor to the square root of the number
            factor = int(num**0.5)
    # If the number is prime, print it
    if is_prime and num > 1:
        print(num)
