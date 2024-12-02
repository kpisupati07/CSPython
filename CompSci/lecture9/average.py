# PROBLEM:
# Write a function average_grade(scores) that takes a dictionary
# of test and homework values and returns the average score.
# Assume they are weighted equally. For example, if
# scores = {
#   'exam1' : 80,
#   'exam2' : 90,
#   'homeworks' : 85
# }
# then average_grade(scores) should return 85.0

def average_grade(scores):
    total_score = 0
    for _, score in scores.items():
        total_score += score
    return total_score/len(scores)

def main():
    scores = {
      'exam1' : 80,
      'exam2' : 90,
      'homeworks' : 85
    }
    average = average_grade(scores)
    print("The average is", average)

if __name__ == "__main__":
    main()


