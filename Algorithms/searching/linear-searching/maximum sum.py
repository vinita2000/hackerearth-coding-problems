# Write your code here
n = int(input())
arr = [int(x) for x in input().split(" ")]
total = 0
cnt = 0
for i in range(n):
    if arr[i] >= 0:
        cnt += 1
        total += arr[i]

if(cnt == 0):
    total = max(arr)
    cnt += 1

print(total, cnt)
