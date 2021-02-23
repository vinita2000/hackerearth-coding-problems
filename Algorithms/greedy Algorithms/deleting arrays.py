
# Write your code here
for t in range(int(input())):
    n,k = [int(x) for x in input().split(" ")]
    cnt = 0
    p = n%(k*2+1)
    if p == 0:
        print(n//(k*2+1))
    else:
        print(n//(k*2+1)+1)

    
