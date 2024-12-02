N=int(input('I will compute the sum of even integers from 2 through?'))
sum=0
for i in range(2,(N+2),2):
    sum=sum+i
print(sum)