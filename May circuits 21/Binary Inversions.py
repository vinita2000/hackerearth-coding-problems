# Write your code here
n,a,x = input().split()
n = int(n)
zeros = int(a)
inv = int(x)
ones = n - zeros

result = ''
for i in range(n):
    if inv >= ones:
        if zeros > 0:
            result += '0'
            inv -= ones
            zeros -= 1
        else:
            break
    else:
        if ones > 0:
            result += '1'
            ones -= 1
        else:
            break

if inv == 0:
    for i in range(zeros):
        result += '0'

    for i in range(ones):
        result += '1'

    for i in range(len(result)-1, -1,-1):
        print(result[i], end=' ')
else:
    print('-1', end=' ')
