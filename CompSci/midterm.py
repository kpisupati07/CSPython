def similar_height(feet1, inches1, feet2, inches2):
    x = feet1*12
    y = feet2*12
    x += inches1
    y += inches2
    return (abs(x-y)<=3)

print(similar_height(6, 1, 6, 6))
