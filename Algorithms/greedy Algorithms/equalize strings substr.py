
# Write your code here
n = int(input())
a = [bool(x=='1') for x in input()]
b = [bool(x=='1') for x in input()]

# print(a, b)
cost = 0

for i in range(n):
    if a[i] != b[i]:
        for j in range(i, n):
            if a[j] == b[j]:
                i = j
                break
            else:
                # flip substr
                a[i] = not a[i]
                i = j+1
        cost += 1
       
print(cost)
