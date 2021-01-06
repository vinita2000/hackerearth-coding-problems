
# Write your code here
for t in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split(" ")] 

    arr.sort()
    print(arr[0]+arr[n-1])
