

import math
# Calculating measures of centrality
data = [19, 28, 34, 36, 37, 43, 44, 44, 46, 47, 48, 51, 52, 54, 55, 55, 56, 59, 60, 62, 62, 65, 66, 68]

n = len(data)
print(n)
sum1 = 0
x = 0
while x < n:
    sum1 = data[x] + sum1
    x += 1
mean = sum1 / n
print("Mean = ", mean)

# finding median of the data :

if n % 2 == 0:
    p = int(n/2)
    x = data[p-1]
    y = data[p]
    median = (x+y)/2
    print("Median = ", median)
else:
    p = int((n+1)/2)
    median = data[p-1]
    print("Median = ", median)

# Find Mode :

count = []
sort = []
for x in data:
    c = 0
    if x in sort:
        continue
    for y in data:
        if x == y:
            c += 1
    count.append(c)
    sort.append(x)
print("Count ", count)
print("sort ", sort)
mode = []
for g in range(len(count)):
    if count[g] == max(count):
        mode.append(sort[g])
print("Mode = ", mode)

# Finding variance and standard deviation:

var1 = [(x-mean)**2 for x in data]
print(var1)
var3 = sum(var1)
print(var3)
var2 = sum(var1)/(n-1)
print("Variance", var2)

print("Variance =", sum([(x-mean)**2 for x in data]) / (n-1))

# Standard deviation

sd = math.sqrt(var2)
print("Standard Deviation =", sd)

# Z score

z = [(x-mean)/sd for x in data]
print(z)
print(sum(z))
zmean = sum(z)/len(z)
print("zmean = ", int(zmean))
zvar = sum([(x - zmean)**2 for x in z]) / (len(z)-1)
print("zvar", zvar)

# Finding percentile
p = 25
lp = (p/100)*(n+1)
print("lp", lp)
Q1yp = data[int(lp)-1]+(lp-int(lp))*(data[int(lp)]-data[int(lp)-1])
print("Q1 or 25th Percentile is = ", Q1yp)

p = 75
lp = (p/100)*(n+1)
print("lp", lp)
Q3yp = data[int(lp)-1]+(lp-int(lp))*(data[int(lp)]-data[int(lp)-1])
print("Q3 or 75th Percentile is = ", Q3yp)
print("IQR = ", Q3yp-Q1yp)

