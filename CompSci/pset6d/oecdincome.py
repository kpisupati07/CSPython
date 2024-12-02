import csv
import scipy.stats
import matplotlib.pyplot

income = []
lifeexp = []

reader = csv.DictReader(open("oecd.csv"))

for row in reader :
   income.append(float(row['Per capita income']))
   lifeexp.append(float(row['Life expectancy']))

r = scipy.stats.linregress(lifeexp, income)
slope = r[0]
intercept = r[1]
correlation = r[2]
print("Correlation coefficient: %f" % correlation)

matplotlib.pyplot.scatter(lifeexp, income)

x1 = min(lifeexp)
y1 = intercept + slope * x1
x2 = max(lifeexp)
y2 = intercept + slope * x2
s = ("Correlation coefficient: %f" % correlation)
avgx =(x1+x2)/2
avgy =(y1+y2)/2
matplotlib.pyplot.xlabel("Life expectancy (years)")
matplotlib.pyplot.ylabel("Per Capita Income")
matplotlib.pyplot.title("Life expectancy vs Per Capita Income")
matplotlib.pyplot.text(avgx, avgy, s, fontdict=None)
matplotlib.pyplot.plot([x1,x2], [y1,y2])
matplotlib.pyplot.savefig("lr_income_life.png")
