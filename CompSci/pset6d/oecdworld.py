import csv
import scipy.stats
import matplotlib.pyplot

population = []
size = []

file1 = open('worldarea.txt', 'r')
Lines1 = file1.readlines()

file2 = open('worldpop.txt', 'r')
Lines2 = file2.readlines()

for i in Lines1 :
    words = i.split ()
    for word in words:
        if word.isdigit():
            word = int(word)
            size.append(word)


for x in Lines2:
    words = x.split ()
    for word in words:
        if word.isdigit():
            word = int(word)
            population.append(word)



r = scipy.stats.linregress(size, population)
slope = r[0]
intercept = r[1]
correlation = r[2]
print("Correlation coefficient: %f" % correlation)

matplotlib.pyplot.scatter(size, population)

x1 = min(size)
y1 = intercept + slope * x1
x2 = max(size)
y2 = intercept + slope * x2
s = ("Correlation coefficient: %f" % correlation)
avgx =(x1+x2)/2
avgy =(y1+y2)/2
matplotlib.pyplot.xlabel("Size")
matplotlib.pyplot.ylabel("Population")
matplotlib.pyplot.title("Population vs Size")
matplotlib.pyplot.text(avgx, avgy, s, fontdict=None)
matplotlib.pyplot.plot([x1,x2], [y1,y2])
matplotlib.pyplot.savefig("lr_size_pop.png")
