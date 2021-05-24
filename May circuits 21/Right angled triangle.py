for t in range(int(input())):
    side = int(input())
    side2 = side*side
    limit = (side*side-1)//2 + 1
    sol = set()
    for x in range(1,limit+1):
        h = pow(x*x+side2,1/2)
        if h.is_integer():
            x = int(x)
            h = int(h)
            if x>h: 
                sol.add((h,x))
            else:
                sol.add((x,h))
    limit1 = int(side//pow(2,1/2) + 1)
    for x in range(1,limit1+1):
        y = pow(side2-x*x,1/2)
        if y.is_integer() and y != 0:
            x = int(x)
            y = int(y)
            if x>y: 
                sol.add((y,x))
            else:
                sol.add((x,y))

    #print(sol)
    print(len(sol))
