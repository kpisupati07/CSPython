# PROBLEM: Write a linear search function
# that scans through a list and returns
# where the given value can be found
# or -1 if not found

def search(a, value):
    for i in range(len(a)):
        if value == a[i]:
            return i
    else:
        return ('-1')

def main():
    a =  [ 1, 3, 4, 9, 11, 99, -1, 0 ]
    print(a)
    print(search(a, 9))   # should print 3
    print(search(a, 12))  # should print -1

if __name__ == "__main__":
    main()
