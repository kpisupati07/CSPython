# PROBLEM: What is wrong with this program that prints
# a congratulations message if the exam average is more than 90?
# How would you fix it?

def average(a, b):
    '''Computes the average of a and b'''
    print((a+b)/2)

def main():
    exam1 = int(input('Exam 1 score: '))
    exam2 = int(input('Exam 2 score: '))
    if (average(exam1, exam2) > 90):
        print('Congrats! You eared honors!!')


if __name__ == "__main__":
    main()
