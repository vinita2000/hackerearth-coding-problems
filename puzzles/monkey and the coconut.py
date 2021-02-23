
# Write your code here
for t in range(int(input())):
    n,k = [int(x) for x in input().split(" ")]
    for i in range(10000):
        a = i*5+1
        if a%4 == 0:
            a = a//4
            b = 5*a+1
            #print("i", i)
            #print("a",a)
            if b%4 == 0:
                b = b//4
                c = 5*b+1
                #print("b",b)
                if c%4 == 0:
                    c = c//4
                    d = 5*c+1
                    #print("c",c)
                    if d%4 == 0:
                        d = d//4
                        e = 5*d+1
                        #print("d", d)
                        if e%4 == 0:
                            e = e//4
                            print("i",i)
                            print("a",a)
                            print("b",b)
                            print("c",c)
                            print("d",d)
                            print("e",e)
                            print("output: ", 5*e+1)
                            break

            
    
