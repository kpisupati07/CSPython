def iter_mult(x, y):

    product = 0
    for i in range(y):
        product = product + x
    return product

def recur_mult(x, y):

    # Base case
    if y == 0 or x == 0:
        return 0

    # Recursive call that gets you closer to the base case
    elif x > 0 and y > 0:
        return x+(iter_mult(x,y-1))

    elif x < 0 or y < 0:
        return -1*(x+iter_mult(abs(x), abs(y)-1))


def main():

    x = 4
    y = 1
    print(iter_mult(x, y))
    print(recur_mult(x, y))

main()