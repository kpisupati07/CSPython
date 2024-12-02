"""Add your solution to the problem 'real_estate' here."""


def is_vowel(c):
    """Returns true if c is an upper- or lower-case vowel character"""
    vowels = "aeiouAEIOU"
    # checks if c is a vowel
    if vowels.count(c) > 0:
        return True
    else:
        return False


def devowel(ad):
    """Takes the text ad and returns a string with
    non-initial vowels removed. The letter 'y' is not considered a
    vowel."""
    result = ""
    prev_space = False#assumes it dosent start with a space
    x = 0
    for c in range(len(ad)):
        # gets each character
        char = ad[c]
        # if it has a space before it, or is the first, because of x = 0 then it should be added to the final
        if is_vowel(char) and (prev_space or x == 0):
            result += char
            prev_space = False
        elif not is_vowel(char):  # if not a vowel, it adds it to the final result.
            result += char
            # if it is a space, prev_space becomes True, so the next time it loops, the next character knows theres a space before it
            prev_space = char == " "
        x += 1
    return result


def main():
    description = input("Enter a description of a property: ")
    print("The advertisement is:", devowel(description))


if __name__ == "__main__":
    main()
