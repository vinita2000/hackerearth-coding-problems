# Write your code here

for t in range(int(input())):
    n,k = (input().split(" "))
    arr = list(map(int,input().split(" ")))
    n = int(n)
    k = int(k)

    k_mod = k % n
    
    arr = arr[::-1]
    #reverse list after k_mod
    arr[k_mod:n] = arr[k_mod:n][::-1]
    #reverse list till k_mod
    arr[:k_mod] = arr[:k_mod][::-1]
    
    for item in arr:
        print(item, end=" ")
    print("\n")
