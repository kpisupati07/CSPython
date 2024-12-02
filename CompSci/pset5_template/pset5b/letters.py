"""Add your solution to the problem 'letters' here."""


def missing_letters(word_list):
    """Takes a word list and returns a sorted
    list of letters, capitalized that do not appear
    in the list.
    """
    letters = set()
    for i in word_list:
        for x in i:
            letters.add(x.upper())
    return letters




def main():
    # Add your solution to the problem that makes use of the above.
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    x = missing_letters(["Now", "is", "the", "TIME"])
    for i in x:
        if i in alphabet:
            alphabet.remove(i)
    print(alphabet)



if __name__ == "__main__":
    main()
