
# Write your code here
for t in range(int(input())):
    n, m = input().split(" ")
    n = int(n)
    m = int(m)

    arr1 = list(map(int, input().split(" ")))
    arr2 = list(map(int, input().split(" ")))

    for i in arr2:
        arr1.append(i)
    
    arr1.sort(reverse=True)
    for item in arr1:
        print(item, end=" ")
    print("\n")
