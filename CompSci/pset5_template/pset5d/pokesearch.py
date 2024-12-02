# Valid traits for Pokemon
import pokedex

TRAITS = ["HP", "Attack", "Sp. Attack", "Sp. Defense", "Speed"]


def english_name(pokemon):
    """OPTIONAL:
    You can use this as a sorting key function for Pokemon"""
    return pokemon["name"]["english"]


def pokesearch(trait, minimum, maximum):
    """
    Returns a list of Pokemon data structures (dictionaries,
    as shown in the pset problem description) that
    have a value of trait between minimum and maximum
    """
    result = []
    for pokemon in pokedex.data:  # gets the data
        value = pokemon["base"][trait]  # sets value to desired trait
        if minimum <= value <= maximum:  # checks if value is within the range
            result.append(pokemon)  # makes a list of dictionaries
    return result


def main():
    trait = input(
        "What Pokemon trait would you like to search on? Valid traits are HP, Attack, Sp. Attack, Sp. Defense, Speed: "
    )  # gets desired trait
    minimum = int(input(f"What is the minimum value for {trait}? "))
    maximum = int(input(f"What is the maximum value for {trait}? "))
    x = pokesearch(trait, minimum, maximum)
    for pokemon in x:  # goes through each item in the list, each dictionary seperately
        name = pokemon["name"]["english"]
        value = pokemon["base"][trait]
        print(
            f"{name} {' ' * (20 - len(name))} {value}"
        )  # prints it formatted because some words are longer than others


if __name__ == "__main__":
    main()
