N= int(input('how many rows should there be?: '))

for i in range(N,0,-1):#makes sure that it will go from Big to small by making spaces increase as it goes down
    print(' '*(N-i), end='')#prints spaces before *
    print('*'*i)