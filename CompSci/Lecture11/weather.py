from sys import argv


def main():
    if len(argv) != 2:
        print("Sorry, Correct usage is to type python weather.py input-file")
        return
    with open(argv[1]) as input_file:
        previous = float(input_file.readline())
        for line in input_file:
            next = float(line)
            print(f'{previous} to {next} change = {next - previous:.1f}')
            previous = next


main()
