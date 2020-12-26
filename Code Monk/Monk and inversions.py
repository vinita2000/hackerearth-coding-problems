
# Write your code here

for t in range(int(input())):
    lst = []
    cnt = 0
    n = int(input())
    for i in range(n):
        row = list(map(int, input().split(" ") ))
        lst.append(row)
   
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if(i<=p and j<=q):
                        if(lst[i][j] > lst[p][q]):
                            cnt += 1

    print(cnt)
    
