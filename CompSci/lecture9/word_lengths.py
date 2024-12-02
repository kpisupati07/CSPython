# PROBLEM: Use list comprehension and the split method
# to compute the average word length in a string
# (don't worry about punctuation). Hint: also use sum.

def average_word_lengths(text):
    words = text.split()
    lengths = [ len(x) for x in words]
    return sum(lengths) / len(words)

def main():
    print(average_word_lengths('The quick brown fox'))

if __name__ == "__main__":
    main()
