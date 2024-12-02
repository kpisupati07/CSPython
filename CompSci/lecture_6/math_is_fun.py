# QUESTION:
# How can we make this module not run main when it is imported?

PI = 3.14159

def area(r):
    ''' returns the area of a circle '''
    return PI*r*r

def main():
    a = area(r=3)
    print(f"The area of the circle is {a}")

main()

