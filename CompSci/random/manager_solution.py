import csv

with open("employees.csv", "r") as file:
    # "hardwiring" the file name is bad style!
    reader = csv.DictReader(file)  # reads file
    manager_dict = {
        "Andrew Adams": 1,
        "Laura Callahan": 2,
        "Nancy Edwards": 3,
        "Steve Johnson": 4,
        "Robert King": 5,
        "Michael Mitchell": 6,
        "Margaret Park": 7,
        "Jane Peacock": 8,
    }
    x = 1
    manager = {}

    for row in reader:  # gets each line seperately
        if row["FirstName"] + " " + row["LastName"] not in manager_dict:
            manager_dict[
                row["FirstName"] + " " + row["LastName"]
            ] = x  # makes dictionary with each person to a number
        if row["Manager"] != "":  # exception of no manager
            print(
                x,
                ",",
                manager_dict[row["Manager"]],
                ",",
                row["LastName"],
                ",",
                row["FirstName"],
                sep="",
            )
        else:  # puts no number for no manager
            print(x, ",", ",", row["LastName"], ",", row["FirstName"], sep="")
        x += 1
