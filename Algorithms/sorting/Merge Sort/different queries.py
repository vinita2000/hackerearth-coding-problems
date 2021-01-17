
# Write your code here
n,q = input().split(" ")
n = int(n)
q = int(q)
arr = [int(x) for x in input().split(" ")]

query1n = []
query1p = []
query2 = []

for i in range(q):
    query = [int(x) for x in input().split(" ")]
    if query[0] == 1 and query[3]<0:
        query1n.append(query)
    elif query[0] == 1 and query[3]>=0:
        query1p.append(query)
    else:
        query2.append(query)
    
#sort all the query lists
query2.sort(key=lambda query2:query2[3])

#negatives of 1
for query in query1n:
   for i in range(query[1]-1, query[2]):
        arr[i] += query[3] 

#all of 2
for query in query2:
    for i in range(query[1]-1, query[2]):
        arr[i] = query[3] 

#positives of 1
for query in query1p:
    for i in range(query[1]-1, query[2]):
        arr[i] += query[3] 


print(*arr, sep=" ")
