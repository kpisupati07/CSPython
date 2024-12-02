# Add your solution to the problem "longer" to this file.
# I clicked style 50 again and i dont know why it formatted the prints like it is, but I was told to use the style 50 format so I am going to keep it

def print_longer(A, B):
    list_1 = (
        A.split()
    )  # splits each term in the list by a space so that each character in a word is not used as a term in the list and turns it into a list
    list_2 = B.split()  # same as the one above
    if len((list_1)) > len(list_2):
        full_list_1 = ", ".join(
            list_1
        )  # makes the list get printed in a format where each term is seperated by a comma
        print(
            f"[{full_list_1}] is the longer list and its last element is {list_1[len(list_1)-1]}"
        )  # to find last element in the list I did -1 so that it gives the last term

    elif len(list_1) < len(list_2):
        full_list_2 = ", ".join(
            list_2
        )  # makes the list get printed in a format where each term is seperated by a comma
        print(
            f"[{(full_list_2)}] is the longer list and its last element is {(list_2[len(list_2)-1])}"
        )

    else:
        print("The lists are the same length!")


# add your run your main function here:
def main():
    X = str(input("input a list seperated by spaces: "))
    Y = str(input("input a list seperated by spaces: "))
    print_longer(X, Y)


main()
