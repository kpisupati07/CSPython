# PROBLEM: Use a function to simplify this duplicated
# (and buggy!) code

def far_to_C(f):
    return (f - 32) * 5 / 9

def main():
    f1=77
    c1=far_to_C(f1)

    f2=95
    c2=far_to_C(f2)
    print(f'{f1} is {c1} in Celsius')
    print(f'{f2} is {c2} in Celsius')



if __name__ == "__main__":
    main()


