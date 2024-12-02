from matplotlib import pyplot as plt
import random

# Example of some bar and scatter plots

# Bar plot of a sorted array.
# The first parameter sets the indices, the second sets the values
x = [i for i in range(10)]
plt.bar(x, x)
plt.xticks(x)
plt.yticks(x)
plt.savefig('bar_sorted')
plt.close()

# Bar plot of a scrambled array.
y = [i for i in range(10)]
random.shuffle(y)
plt.bar(x, y)
plt.xticks(x)
plt.yticks(x)
plt.savefig('bar_scrambled')
plt.close()

x = [i for i in range(10000)]

# Scatter plot of a sorted array 
plt.scatter(x, x, s=1) # s = 1 sets the point size
plt.savefig('scatter_sorted')
plt.close()

# plots an out of order array
y = [i for i in range(10000)]
random.shuffle(y)
plt.scatter(x, y, s=1) # s = 1 sets the point size
plt.savefig('scatter_scrambled')
plt.close()






