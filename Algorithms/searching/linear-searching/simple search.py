
# Write your code here
import sys
n = int(input())
lst = list(int(num) for num in input().strip().split())[:n]
k = int(input())

if(n <= 0 or n >10000 or k <= 0 or k >10000000000):
    sys.exit()

for i in range(n):
    if lst[i]<=0 or lst[i]>10000000000:
        sys.exit()

for i in range(n):
    if lst[i] == k:
        print(i)
        break
