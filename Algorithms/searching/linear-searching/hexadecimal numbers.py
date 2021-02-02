
# Write your code here
import math 
def GetHexSem(num):
    hexSum = 0
    while num >= 16:
        hexSum += num%16
        num = int(num/16)
    return hexSum+num

for t in range(int(input())):
    l, r = [int(x) for x in input().split(" ")]
    cnt = 0
    for i in range(l, r+1):
        sumH = GetHexSem(i)
        #gcd of sumH and i
        currGCD = math.gcd(i, sumH)
        if currGCD > 1:
            cnt += 1
    print(cnt)
    
