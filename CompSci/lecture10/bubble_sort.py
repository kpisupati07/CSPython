# PROBLEM: Finish implementing bubble sort using swap, by adding
#          the inner loop.

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def bubble_sort(a):
    ''' Sorts the list a '''
    for i in range(len(a)):
        for j in range(len(a)-1):                # <--- use the print to help you debug
            if a[j] > a[j+1]:
                swap(a, j, j+1)
                print(a)

def main():
    a = [ 2, 1, 9, 7, 6, 4, 8, 3, 5 ]
    bubble_sort(a)
    print(a)


if __name__ == "__main__":
    main()
