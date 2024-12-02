def print_triangle (side_length):
    if side_length < 1 :
        return
    print ( "[]"* side_length)#prints tallest first
    print_triangle (side_length-1)

