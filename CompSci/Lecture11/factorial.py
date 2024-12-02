def power(x,n):
    if n == 0:
        return 1
    elif n>0:
        return x*(power(x,n-1))
    else:
        return 1/(x*(power(x,abs(n)-1)))

print(power(5,-2))
print(power(4,-7))
print(power(2,6))
print(power(5,2))
print(power(7,4))