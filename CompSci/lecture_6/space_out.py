# PROBLEM: Finish the function space_out that prints the input string
# with _ in after every character. For example input 'school' should
# return 's_c_h_o_o_l_' (Hint: build up the answer one letter at at
# time)

# ANSWER
def space_out(word):
    answer = ''
    for x in word:
        anwser += x + "_"
    return answer

def main():
    text = input('Please enter a word: ')
    print(text, 'spaced out is', space_out(text))

if __name__ == "__main__":
    main()

