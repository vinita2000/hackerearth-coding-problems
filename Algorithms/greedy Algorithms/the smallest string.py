# Write your code here
# Write your code here
for t in range(int(input())):
    n,k = input().split(" ")
    s = [(x) for x in input()]
    n = int(n)
    k = int(k)
    
    for i in range(n):
        if k > 0:
            if s[i] != 'a':
                order = ord('z') - ord(s[i]) + 1
                if k >= order :
                    # it is cyclic
                    k -= (order)
                    s[i] = 'a' # till a
        else:
            break

    if k > 0:
        mod = k % 26 # will be same at +27
        if ord(s[n-1])+mod > ord('z'):
            order = ord(s[n-1]) + mod - ord('z')
            s[n-1] = chr(ord('a')+order - 1)
        else:
            s[n-1] = chr(ord(s[n-1]) + mod)

    print(*s, sep='')
