# Jet Blue's checked bag fees for a basic fare are:
#
# First bag $35
# Second bag $45
# Third (or more) bag $150
#
# PROBLEM:
# Write a function baggage fee that takes
# the number of checked bags as input and
# returns the baggage fee. Assume the input is
# a non-negative integer

def baggage_fee(num):
    if num == 1:
        return 35
    if num == 2:
        return 35+45
    else:
        return ((num-2)*150)+35+45

def main():
    num = int(input("How many bags? "))
    print(f"The baggage fee for {num} bags is", baggage_fee(num))

if __name__ == "__main__":
    main()

