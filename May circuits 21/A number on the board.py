
# Write your code here
import math

a,b,c = input().split(" ")
a = float(a)
b = int(b)
c = int(c)

n = 1.0

if a>=0 and a<=1:
    n = round(math.log(1+b*c, 2), 8)

elif a > b:
    n = round(c*(math.log(a, 2)), 8)

else:
    n = (1+b-a)/(b*(a-1))
    n = int(n) + 1
    n = round( math.log(1+n*b, 2) + (c-n)*(math.log(a, 2)), 8 )

print(n)
