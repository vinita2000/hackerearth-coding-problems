
# Write your code here
n = int(input())
arr = [int(x) for x in input().split(" ")]
arr.sort()
maxSum = 0
minSum = 0
total = 0
for val in arr:
    total += val

maxSum = total - arr[0]
minSum = total - arr[n-1]
print(minSum, maxSum)
