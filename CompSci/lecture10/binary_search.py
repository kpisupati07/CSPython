# EXAMPLE: The binary search algorithm
def search(a, value):
    low = 0
    hi = len(a) - 1
    while low <= hi:
        mid = (low + hi) // 2
        if value == a[mid]:
            return mid
        elif value > a[mid]:
            low = mid + 1
        else:
            hi = mid - 1
    return -1

def main():
    a =  [ 1, 3, 4, 9, 11, 99, -1, 0 ]
    a.sort()
    print(a)
    print("9 is at position:", search(a, 9))    # should print 3
    print("12 is at position:", search(a, 12))  # should print -1


if __name__ == "__main__":
    main()
