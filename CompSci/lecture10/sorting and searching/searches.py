def linear_search(a, value):
  for i in range(len(a)):
    if a[i] == value:
      return i
  return -1

def binary_search(a, value):
    low = 0
    hi = len(a) - 1
    while low <= hi:
        mid = (low + hi) // 2
        value_at_mid = a[mid]
        if value == value_at_mid:
            return mid
        elif value > value_at_mid:
            low = mid + 1
        else:
            hi = mid - 1
    return -1
