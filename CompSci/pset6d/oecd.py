import csv
import scipy.stats
import matplotlib.pyplot

lifeexp = []
healthex = []

reader = csv.DictReader(open("oecd.csv"))

for row in reader :
   if row['Country'] == 'United States':#removes outlier
      continue
   lifeexp.append(float(row['Life expectancy']))#adds to the list
   healthex.append(float(row['Health expenditures']))

r = scipy.stats.linregress(healthex, lifeexp)
slope = r[0]
intercept = r[1]
correlation = r[2]
print("Correlation coefficient: %f" % correlation)

matplotlib.pyplot.scatter(healthex, lifeexp)

x1 = min(healthex)
y1 = intercept + slope * x1
x2 = max(healthex)
y2 = intercept + slope * x2
s = ("Correlation coefficient: %f" % correlation)
avgx =(x1+x2)/2
avgy =(y1+y2)/2
matplotlib.pyplot.xlabel("Health expenditures")
matplotlib.pyplot.ylabel("Life expectancy (years)")
matplotlib.pyplot.title("Life expectancy vs health expenditures")
matplotlib.pyplot.text(avgx, avgy, s, fontdict=None)
matplotlib.pyplot.plot([x1,x2], [y1,y2])
matplotlib.pyplot.savefig("lr_no_us.png")
