# PROBLEM:  What values are stored in the list a after the loop has run?

def main():
    a = [ 1, 7, 5, 6, 4, 14, 11 ]
    for i in range(len(a) - 1):
        if (a[i] > a[i + 1]):
            a[i + 1] = a[i + 1] * 2
    print(a)

if __name__ == "__main__":
    main()
