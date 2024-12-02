import random

# Swap the elements i and j in list a
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

# returns a list with the numbers 0...(n -1)
# in ascending order
def sorted_list(n):
    return list(range(n))

# returns a list with the numbers 0...(n -1)
# in random order
def random_list(n):
    ans = list(range(n))
    random.shuffle(ans)
    return ans

# returns a representation of the list
# truncated after 100 terms
def to_string_truncated(a):
    if len(a) <= 100:
        return str(a)
    else:
        ans = "[ "
        ans += ", ".join(map(str, a[:100]))
        ans += f" ... truncated list of length {len(a)} ]"
        return ans
