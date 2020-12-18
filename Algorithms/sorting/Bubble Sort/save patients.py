
# Write your code here
n = int(input())
vacc = list(map(int,input().split(" ")))
ptn = list(map(int,input().split(" ")))

res = 'Yes'

for i in range(n):
    if(vacc[i] < ptn[i]):
        res = 'No'

print(res)
