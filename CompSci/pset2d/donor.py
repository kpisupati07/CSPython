def donor():
    #input in float so that it can be decimals
    N= float(input('Write the amount of contribution: $'))
    #makes sure n is not <0 and ends the program if it is
    if N<0:
        print('Sorry, you cant donate Negative amounts!')
        exit()
    #Conditional statements to see what N is
    if 0<=N<15:
        print('Cheapskate!')

    elif 15<=N<200:
        print('Friends!')

    elif 200<=N<1000:
        print('Supporters!')

    elif 1000<=N<10000:
        print('Patrons!')

    else:
        print('Benefactor!')
donor()

