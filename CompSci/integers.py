for N in range(100,1000):
    X = N//100 #gets last digit
    Y = (N-(100*X))//10
    Z = (N-((100*X)+(Y*10)))//1
    if (X**3)+(Y**3)+(Z**3)==N:
        print(N)
    # all digits cubed added together equal the number, only 3 digits