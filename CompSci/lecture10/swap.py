def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def main():
    # PROBLEM: Create a function that
    # Swaps the entries at position i and j of an
    # list
    my_data = [ 12, 22, 3, 3, 45, 4 ]
    swap(my_data, 0, 4)
    print(my_data)
    # Should print [ 45, 22, 3, 3, 12, 4 ]

if __name__ == "__main__":
    main()
