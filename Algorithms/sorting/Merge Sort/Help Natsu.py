
# Write your code here
from collections import OrderedDict 
for t in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())

    dic = {}
    for item in arr:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
        
    srt = list(sorted(dic.items(), key=lambda i :(i[1],i[0]), reverse=True))
    
    srt.reverse()
    for item in srt:
        print(item[1], item[0])
    
