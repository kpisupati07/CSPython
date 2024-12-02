import random


def has_duplicates(birthdays):
    seen = set()
    for birthday in birthdays:  # gets each birthday
        if birthday in seen:
            return True  # is there is a match
        else:
            seen.add(birthday)  # adds not used birthdays to the set
    return False  # if there is no match


simulations = int(input("Enter the number of simulations: "))
students = int(input("Enter the number of students: "))

matches = 0

for i in range(simulations):  # repeats it sumulatios amount of times
    birthdays = [
        random.randint(1, 365) for _ in range(students)
    ]  # picks a birthday for students amount of students
    if has_duplicates(birthdays):
        matches += 1  # if true, +1
print(f"After {simulations} simulations")
print(f"with {students} students")
print(f"there were {matches} simulations with at least one match")
