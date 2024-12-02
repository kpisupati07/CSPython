# PROBLEM: Write a function get_unique_letters that returns a set
# of the unique letters in a string.
#
# get_unique_letters('abracadabra')
# should return
# {'b', 'c', 'r', 'd', 'a'}
#
# And the program should print:
# There are 5 different letters in abracadabra. They are:
# {'b', 'c', 'r', 'd', 'a'}
#
# BONUS: print the letters out in sorted order
 
def get_unique_letters(text):
    ???

def main():
    text = 'Abracadabra'
    letters = get_unique_letters(text)
    print(f'There are {len(letters)} different letters', end='')
    print(f' in {text}. They are:')
    print(letters)

if __name__ == "__main__":
    main()


