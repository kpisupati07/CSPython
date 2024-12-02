from matplotlib import pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

plt.plot(x, y)
plt.title('Squares')
plt.savefig('squares')
plt.close()