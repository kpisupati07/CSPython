# PROBLEM:
# Write a function homework_average(scores) that takes a
# a data-structure of test and homework values and returns
# the average homework score. For example, if
# scores = {
#   'midterm' : 75,
#   'final'   : 95,
#   'homeworks' : [ 80, 90, 75, 99, 100, 100 ]
# }
# then homeword_average(scores) should return 90.67

def homework_average(scores):
    x = scores['homeworks']
    return sum(x)/len(x)

def main():
    scores = {
      'midterm' : 75,
      'final'   : 95,
      'homeworks' : [ 80, 90, 75, 99, 100, 100 ]
    }
    hw_average = homework_average(scores)
    print(f"The homework average is {hw_average:.2f}")


if __name__ == "__main__":
    main()


