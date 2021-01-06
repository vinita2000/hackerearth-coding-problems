
# Write your code here
for t in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    
    #remove unique items from arr
    #append to dictionary
    cnt = 0
    i = n-1
    while i>=0:
        dic = {}
        while i>=0:
            if arr[i] not in dic:
                dic[arr[i]] = arr[i]
                del arr[i]
            i -= 1
        cnt += 1
        i = len(arr)-1

    print(cnt + len(arr))
