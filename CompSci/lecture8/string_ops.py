# PROBLEM: Write a function that takes a string and returns the string
#in lowercase where the words have beensorted by length. Hint:
#remember .split() and .join()

def foo(text):
    words = text.split()
    words.sort(key=len)
    return " ".join(words).lower()

def main():
    print(foo("This is Python"))  # should print 'is this python'

if __name__ == "__main__":
    main()
