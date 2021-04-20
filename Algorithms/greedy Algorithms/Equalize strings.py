
# Write your code here
n = int(input())
a = [int(x) for x in input()]
b = [int(x) for x in input()]

# print(a, b)
cost = 0

for i in range(n-1):
    if a[i] != b[i]:
        # check for swap
        if (a[i+1] == b[i]) and (a[i+1] != b[i+1]):
            # swap 
            a[i], a[i+1] = a[i+1], a[i]
            cost += 1
        else:
            # flip
            if a[i] == 1:
                a[i] = 0
            else:
                a[i] = 1
            cost += 1

if (a[n-1] != b[n-1]):
    cost += 1 
print(cost)
