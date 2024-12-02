def length(word):
    if word == "":
        return 0
    else:
        return 1+(length(word[1:]))
print(length('hello'))