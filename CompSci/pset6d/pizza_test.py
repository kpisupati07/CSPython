# pizza_test.py
from Pizza import Pizza

def main():
    appetizer = Pizza("Pepperoni", 16, 10.50, 10)
    print(appetizer)
    dinner = Pizza("Anchovy & Pineapple", 20, 11.95, 8)
    print(dinner)
    print(dinner.area_per_slice())
    print(appetizer.area_per_slice())
    print(dinner.cost_per_slice())
    print(appetizer.cost_per_slice())
    print(dinner.cost_per_square_inch())
    print(appetizer.cost_per_square_inch())

if __name__ == "__main__":
    main()
