# PROBLEM: Write a function that returns a string in reverse

def reverse_string(word):
    anwser = ''
    for i in range (1, len(word)+1):
        anwser+= word[-i]
    return anwser
def main():
    print(reverse_string('evian'))    # should print naive
    print(reverse_string("stressed"))   # should print desserts

if __name__ == "__main__":
    main()

