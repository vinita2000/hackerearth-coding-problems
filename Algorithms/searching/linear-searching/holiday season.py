
# Write your code here
n = int(input())
st = input()
cnt = 0
dic = {}
for i in range(n):
    temp = []
    for j in range(i+1, n):
        if st[i] == st[j]:
            temp.append(j)
    if(len(temp)):
        dic[i] = temp
#print(dic)
nDic = len(dic)
forCnt = 0
for i in dic.keys():
    if(forCnt < nDic-1):
        forCnt += 1
        for k in range(len(dic[i])):
            end = dic[i][k]
            for j in range(i+1, end):
                if j in dic:
                    for m in range(len(dic[j])-1, -1, -1):
                        if dic[j][m] > end:
                            cnt += 1
                        else:
                            break
print(cnt)
