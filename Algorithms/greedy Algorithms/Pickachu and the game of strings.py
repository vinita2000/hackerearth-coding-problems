
# Write your code here
n = int(input())
s = input()
t = input()
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(ord(s[i])-64)
    arr2.append(ord(t[i])-64)
#print(arr1, arr2)
cnt = 0
for i in range(n):
    diff = arr2[i]-arr1[i]
    if diff < 0:
        diff = 26 - arr1[i] + arr2[i]    

    while diff > 0:
        if diff >= 13:
            arr1[i] += 13
            cnt += 1
            diff -= 13 
        else:
            arr1[i] += 1
            cnt += 1
            diff -= 1 
print(cnt)
