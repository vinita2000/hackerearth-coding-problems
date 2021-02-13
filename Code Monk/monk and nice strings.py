
# Write your code here
n = int(input())
arr = []
for i in range(n):
    arr.append(input())

output = []
output.append(0)
for i in range(1, n):
    cnt = 0
    for j in range(0, i):
        if arr[j] < arr[i]:
            cnt += 1
    output.append(cnt)
 
for val in output:
    print(val)
