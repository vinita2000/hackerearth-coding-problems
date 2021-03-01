import math

n = int(input())
for i in range(n-2, 0, -1):
    gcd = math.gcd(n, i)
    if g == 1:
        print(i)
        break
