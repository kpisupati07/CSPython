def is_palindrome(word):
    word = word.lower()
    if len(word) <= 1:  # base case
        return True
    elif word[0] == word[-1]:  # checks if 1st and last same
        return is_palindrome(word[1:-1])  # suts first and last off, and goes again
    else:
        return False
