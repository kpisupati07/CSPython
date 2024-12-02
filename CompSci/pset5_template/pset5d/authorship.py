"""Add your solution to the problem 'authorship' here."""

from romeo_and_juliet_data import lines  # makes lines a variable for the data


def word_length_histogram(text_list):
    """Takes the a list of multiword lines and returns
    a dictionary where the keys are word lengths and the
    values are how many words there are of that length.
    Assume there is no punctuation to worry about.
    For example, the input:
        [ "Summer school", "is nearly over"]
    should return the dictionary
        { 6 : 3, 2 : 1, 4 : 1 }
    """
    x = {}
    for line in text_list:  # gets each line speerately
        for word in line.split():
            word = word.replace("'", "")  # gets rod of '
            length = len(word)
            if (
                length in x
            ):  # checks if the definition for the letters in thwe word are in the dictiony, and adds a value to it if it is there
                x[length] += 1
            else:  # starts it at 1 because its the first
                x[length] = 1
    return x


def main():
    x = word_length_histogram(lines)
    total_words = sum(
        x.values()
    )  # values are all the number of letters, and it is addded up to get the total for the percentages
    for length in range(1, 15):  # 14 times because opnly 14 letters is the max
        if (
            length in x
        ):  # checks if the dictionary has the length, because it could not have some words
            count = x[length]  # count is the number of words
        else:
            count = 0  # means there was none of that length
        fraction = count / total_words * 100
        print(f"Proportion of {length}- letter words: {fraction:.2f}% ({count} words)")


if __name__ == "__main__":
    main()
