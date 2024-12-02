# PROBLEM: Write a function how_good that rates an ice-cream flavor by
# returning an integer from 0-10, with chocolate getting 10, caramel
# getting 1 and everything else getting 0

def how_good(flavor):
    rating = 0
    if (flavor == "chocolate"):
        rating =10
    elif (flavor == "carmel"):
        rating = 1
    return rating


def main():
    flavor = input('Please enter an ice-cream flavor: ')
    x = 'very ' * how_good(flavor)
    print(f'{flavor} ice-cream is {x}good!' )


if __name__ == "__main__":
    main()
