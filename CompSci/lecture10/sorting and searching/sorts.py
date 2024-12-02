from s7_utils import swap

def bubble_sort(a):
  for i in range(len(a) -1):
    for j in range(len(a) - 1):
      if a[j] > a[j + 1]:
        swap(a, j, j + 1)

def insertion_sort(a):
  for i in range(1, len(a)):
    j = i
    while (j > 0 and a[j-1] > a[j]):
      swap(a, j - 1, j)
      j -= 1

'''
(Advanced - bonus for fun only) One of the fastest sorting
algorithms out there -- Quicksort. 
Based on Sedgewick code

See:
http:#algs4.cs.princeton.edu/23quicksort/
'''
from s7_utils import *

def quick_sort(a):
    qsort(a, 0, len(a) - 1)

# Reorder the list into a low and high region:
# Pick a pivot value
# reorder the list so that everything less than the pivot value
# appears before it in the list
# and everything greater than the pivot value appears after it
# in the list
def partition(a, left, right):
    pivot = a[left]
    pivot_index = left
    i = left
    j = right + 1
    while True:
        i += 1
        while (a[i] < pivot):
            if (i == right):
                break
            i += 1
            
        j -= 1
        while (a[j] > pivot):
            if (j == left):
                break
            j -= 1
            
        if (j <= i):
            break    # we've finished all swapping
        swap(a, i, j)   # the value at i is a high value on
                        # the left side of the list
                        # the value at j is a low value in the
                        # right side of the list, so swap them
    swap(a, j, pivot_index)   # put the pivot in the middle
                              # we had it off to the side
    return j # new_pivot_index

def qsort(a, left, right):
    if right <= left:            # base case of the recursion:
        return
    # Recursive calls! We'll learn about this next week.
    pivot_index = partition(a, left, right)
    qsort(a, left, pivot_index - 1)
    qsort(a, pivot_index + 1, right)


