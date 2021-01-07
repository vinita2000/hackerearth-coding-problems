for t in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split(" ")]
   
    dic = {}
    sortedArr = sorted(arr)
    i = 0
    for val in sortedArr:
        if val not in dic:
            dic[val] = i
            i +=1
    count = 0
    for i in range(0,n,2):
        if (i%2) != (dic[arr[i]]%2):
            count += 1

    print(count)
