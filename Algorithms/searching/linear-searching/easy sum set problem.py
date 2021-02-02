

n = int(input())
a = []
a = [int(x) for x in input().split(" ")]
m = int(input())
c = []
c = [int(x) for x in input().split(" ")]
b = []

minB = min(c)-min(a)
maxB = max(c)-max(a)
b.append(minB)
if(maxB not in b):
    b.append(maxB)

for i in range(m):
    for j in range(n):
        curr = c[i]-a[j]
        if(curr not in b) and (curr>minB) and (curr<maxB):
            b.append(curr)

b.sort()
temp = [] 
temp.append(minB)
if(maxB not in temp):
    temp.append(maxB)

x = len(b)
flag = True
for i in range(1, x-1, 1):
    for j in range(n):
        if ((a[j] + b[i]) in c):
            flag = True
        else:
            flag = False
            break
    if(flag) and (b[i] not in temp):
        temp.append(b[i])

temp.sort()
for item in temp:
    print(item, end=" ")









