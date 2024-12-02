# Add your solution to the problem "congress" here.

# Implement eligible_for_sentate here.
#
# Returns true if the candidate is eligibe to run for senate.
# Does not print anything out.
def eligible_for_senate(age, citizenship):
    if age >= 30 and citizenship >= 9:
        return True
    else:
        return False

# Implement eligible_for_house here.
#
# Returns true if the candidate is eligible for the house.
# Does not print anything out.
def eligible_for_house(age, citizenship):
    if age >= 25 and citizenship >= 7:
        return True
    else:
        return False


# Add a main that tests out your functions as specified in the problem.
def main():
    print(eligible_for_house(37, 3)) 
    print(eligible_for_senate(37, 3))
    print(eligible_for_house(47, 8))
    print(eligible_for_senate(47, 8))

# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
