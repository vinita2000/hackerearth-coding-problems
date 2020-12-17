# Write your code here

n = int(input())    
arr = list(map(int,input().split(" ")))

total = 0

arr.sort()
for i in range(n-1):
    cnt = 0
    j = 0
    while(arr[i] == arr[i+1]):
        cnt = cnt+1
        i = i+1
    total = total + cnt

print(total)
