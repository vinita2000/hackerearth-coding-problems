no_inputs = int (input())

for i in range(no_inputs):
    cur = int(input())
    if cur > 1:
        num = 0
        deno = 2
        resXor = 0
        p = 1
        while cur//deno > 0:
            deno = pow(2,p)

            count = (cur+1)//deno
            count = (count*(deno//2))

            mod = (cur+1)%deno
            if deno > 2 and mod > deno//2:
                count += (mod - (deno//2))

            #print('bitCount ',p,count)
            if count%2 == 1:
                resXor = resXor | (deno//2)

            p+=1

        output = []
        while resXor > 0:
            if resXor >= cur:        
                output.append(cur)
                resXor = resXor - cur
            else:
                output.append(resXor)
                resXor = 0
        print(len(output), *(output))
    else:
        print(1,1)
