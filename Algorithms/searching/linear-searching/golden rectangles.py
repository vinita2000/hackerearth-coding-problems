
# Write your code here
n = int(input())
cnt = 0
for i in range(n):
    w,h = [int(x) for x in input().split(" ")]
    ratio1 = w/h
    ratio2 = h/w
    if (ratio1 >= 1.6 and ratio1 <= 1.7)or(ratio2 >= 1.6 and ratio2 <= 1.7):
        cnt += 1
print(cnt)
