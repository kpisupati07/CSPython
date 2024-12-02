def main():
    # Should print
    # Number of words: 4
    # Number of a:  0
    # Number of e:  1
    # Number of i:  1
    # Number of o:  2
    # Number of u:  1
    print_stats("The quick brown fox")


# PROBLEM: Write a function that prints the number of words
# in the string text, and prints the number of each vowel.
# (not counting y)
# Hint: use the function split.
#       and also use the loop
#           for v in 'aeiou':
def print_stats(text):
    num_words = len(text.split())
    print(f" Number of words: {num_words}")
    for v in "aeiou":
        count = text.lower().count(v)
        print(f"Number of {v}: {count}")


if __name__ == "__main__":
    main()
