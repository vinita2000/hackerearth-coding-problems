m,n,x,q = [int(i) for i in input().split( )]
ndic = {}
for t in range(q):
    query = [int(i) for i in input().split( )]
    if query[0] == 1:
        r,c1,c2 = query[1],query[2],query[3]
        for i in range(r+c1,r+c2+1):
            if i in ndic.keys():
                ndic[i] += 1
            else:
                ndic[i] = 1
        #print(ndic)
        #dic[r+c1:r+c2+1] = map((-1).__add__, dic[r+c1:r+c2+1])
    elif query[0] == 2:
        c,r1,r2 = query[1],query[2],query[3]
        #dic[c+r1:c+r2+1] = map((-1).__add__, dic[c+r1:c+r2+1])
        for i in range(c+r1,c+r2+1):
            if i in ndic.keys():
                ndic[i] += 1
            else:
                ndic[i] = 1
        #print(ndic)
    elif query[0] == 3:
        k = query[1]
        count,ans = 0,0
        if m >= n:
            large = m
            small = n
        else:
            large = n
            small = m 
        t = 1
        for i in range(2,m+n+1):
            freq = 0
            if i <= small:
                freq = i-1
            elif i <= large+1:
                freq = small
            else:
                freq = small-t
                t += 1
            #print(i, freq)
            if i in ndic.keys():
                count += (freq-ndic[i])
            else:
                count += freq
            if k <= count: 
                ans = i
                break
        if ans == 0:
            print(-1)
        else:
            print(ans+x)
