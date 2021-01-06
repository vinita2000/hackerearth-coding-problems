
# Write your code here
n = int(input())
for i in range(n):
    st = list(map(str, input().split(" ")))

    dic = {}
    for i in range(len(st)):
        dic[i] = len(st[i])
   
    temp = {}
    temp = sorted(dic.items(), key=lambda item:item[1])

    output = ''
    output += " "
    for key in temp:
        #print(st[key[0]], end=" ")
        output += st[key[0]]
        output += " "

    print(output)
    
    #print("\n")
    
   
