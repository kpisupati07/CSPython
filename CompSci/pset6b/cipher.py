import sys


def generate_key(string, key):
    key = list(key.upper())
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(
                key[i % len(key)]
            )  # repeatws it and adds it multiple times so that it is the length of the string
        return "".join(key)


def vigenere_cipher(string, key, mode):
    result = ""
    for i in range(len(string)):
        char = string[i]
        if char.isalpha():
            char = char.upper()  # makes all upprecase so that it worksh
            if mode == "encrypt":  # encrypt mode
                result += chr(
                    (ord(char) + ord(key[i % len(key)]) - 2 * ord("A")) % 26 + ord("A")
                )  #
            else:  # decrypt mode
                result += chr((ord(char) - ord(key[i % len(key)])) % 26 + ord("A"))
        else:
            result += char
    return result


def main():
    key = sys.argv[1]
    mode = "encrypt"
    input_file = sys.argv[2]  # gets arguments
    output_file = sys.argv[3]
    if len(sys.argv) > 4 and sys.argv[4] == "-d":  # change mode
        mode = "decrypt"
    with open(input_file, "r") as f:  # reads input file
        string = f.read()
    key = generate_key(string, key)
    result = vigenere_cipher(string, key, mode)
    with open(output_file, "w") as f:  # makes new output file
        f.write(result)


main()
