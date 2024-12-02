args = (input("Enter integers separated by spaces: ")).split()
total = sum(
    [int(x) for x in args]
)  # gets each int seperately, then adds them into the total variable
print(f"The sum of the args is: {total}")
