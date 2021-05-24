def ap(a,d,x):
    n = (x-a)/d + 1
    if n.is_integer():
        return int(n)
    else:
        return int(n+1)

def ap1(a,d,x):
    n = (x-a)/d + 1
    if n.is_integer():
        return int(n)
    else:
        return int(n)

tests = int(input())
for test in range(tests):
    L,R = input().split()
    L = int(L)
    R = int(R)
    cnt = 0
    #print('******')
    for i in range(1,int(pow(R,1/2))+1):
        a = i*i
        n1 = 0
        n2 = 0
        if L >= a:
            n1 = ap(a,2*i,L)
        if R >= a:
            n2 = ap1(a,2*i,R)
        else:  
            break

        cnt = cnt + (n2 - n1)
        if n1!=0:
            cnt += 1

    print(cnt)
