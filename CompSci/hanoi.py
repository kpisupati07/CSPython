def towers (origin, dest, intermed, num_disks):
    if num_disks == 1: # base case
        print ("Move disk #1 from " + origin + " to " + dest )
        return
    else: # recursive case
        towers (origin, intermed, dest, num_disks-1)
        print ("Move disk #" + str(num_disks) + " from " + origin + " to " + dest)
        towers (origin, intermed, dest, num_disks-1)
        return

towers('Left', 'Right', 'Middle', 3)