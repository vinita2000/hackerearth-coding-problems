
# Write your code here
for t in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split(" ")]
    dic = {}
    for i in range(n):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    temp = {}
    temp = sorted(dic.items(), key=lambda item: item[1])
    #print(dic,'\n', temp)

    tempLen = len(temp)
    if tempLen > 1:
        n2, n1 = temp[0][1], temp[tempLen-1][1]
        if n1-n2>0:
            print(n1-n2)
        else:
            print(1)

    else:
        print(-1)




