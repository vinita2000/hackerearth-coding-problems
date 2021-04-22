
# Write your code here
n,k = input().split(" ")
arr = [int(x) for x in input().split(" ")]
n = int(n)
k = int(k)

arr.sort()

cnt = 0

for i in range(1, n-1):
    if arr[i-1] >= arr[i]-k:
        cnt += 1
        continue
    elif arr[i+1] <= arr[i]+k:
        cnt += 1
        continue
     
# for arr[0] and arr[n-1]
if arr[1] <= arr[0]+k:
    cnt += 1
 
if arr[n-2] >= arr[n-1]-k:
    cnt += 1

print(cnt, "students need to worry!")
print(n-cnt, "students should relax!")

