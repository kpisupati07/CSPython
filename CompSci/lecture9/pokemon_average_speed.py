# PROBLEM: Write a main function that reads in the full pokedex from
# pokedex.py and prints the average speed of all the pokemon.
#
# Hint:
#  - iterate through the dictionary and sum up speed data
import pokedex

def main():
    total_speed = 0
    for pokemon in pokedex.data:
        total_speed += (pokemon['base']['Speed'])
    print (total_speed/len(pokedex.data))

if __name__ == "__main__":
    main()
