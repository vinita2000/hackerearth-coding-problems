
# Write your code here
n = int(input())
arr = [int(x) for x in input().split(" ")]
k = int(input())

dic = {}
for i in range(n):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

temp = []
for item in dic:
    if dic[item] == k:
        temp.append(item)

temp.sort()
print(temp[0])
