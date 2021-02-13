
# Write your code here
st, k = input().split(" ")
k = int(k)
temp = []
n = len(st)
for i in range(n):
    temp.append(st[i:n])

temp.sort()
print(temp[k-1])
