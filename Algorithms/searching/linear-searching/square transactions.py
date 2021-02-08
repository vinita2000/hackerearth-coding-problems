
# Write your code here

def matchTarget(tran, query, i, j):
    if j-i <= 10:
        return i, j
    else:
        mid = i + int((j-i+1)/2)
        if tran[mid] >= query:
            return matchTarget(tran,query, i, mid)
        else:
            return matchTarget(tran,query, mid+1, j)
        
    

t = int(input())
tran = [int(x) for x in input().split(" ")]
q = int(input())

for i in range(1,t):
    tran[i] = tran[i-1] + tran[i]

for i in range(q):
    isAchieved = -1
    query = int(input())
    p,q = matchTarget(tran, query, 0, t-1)
    for j in range(p, q+1):
        if tran[j] >= query:
            isAchieved = j+1
            break
    print(isAchieved)



        
