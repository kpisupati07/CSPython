"""Add your solution to the problem 'alphabetical' here."""


def alphabetical(words):
    """Takes the a list of words and returns a list of strings
    with each of the letters in each word sorted in alphabetical
    (not unicode!) order.
    For example, the for the parameter
    ['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']
    the return value should be
    ['aelpp', 'ikmnppu', 'glo', 'eiRrv', 'fox', 'dnop']
    """

    # Define a function that sorts each word in a list of words in alphabetical order
    def sort_word(word):
        chars = list(word)  # makes it into list of letters
        n = len(chars)
        for i in range(n):
            for j in range(n - i - 1):  # makes it not sort already sored letters again
                # see if one word is earlier in the alphabet than another
                if ord(chars[j].lower()) > ord(chars[j + 1].lower()):
                    # swithces order of them if its out of order
                    chars[j], chars[j + 1] = chars[j + 1], chars[j]
        # makes it back into a string
        return "".join(chars)

    sorted_words = []
    for i in range(len(words)):
        # get each word
        word = words[i]
        # sorts words, and then put it into a list
        sorted_words.append(sort_word(word))
    return sorted_words


def main():
    words = []
    # get the input from the user 5 times
    for i in range(6):
        # add words to list
        input_word = input(f"Enter word {i + 1}: ")
        words.append(input_word)
    # sorts and then prints
    sorted_words = alphabetical(words)
    print(sorted_words)


if __name__ == "__main__":
    main()
