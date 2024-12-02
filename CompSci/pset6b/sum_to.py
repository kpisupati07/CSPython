def sum_to(n):
    if n == 0:  # base case
        return 0.0
    elif n < 0:
        print("Error: n must be a positive integer")
        return None
    else:  # recursive case, keeps callling function addind 1/ 1 less every time, so 1/5+ 1/5-1 and so on
        return 1 / n + sum_to(n - 1)
