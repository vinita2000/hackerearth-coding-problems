
# Write your code here
n = int(input())    
arr = list(map(int,input().split(" ")))

def bubbleSort(arr):
    cnt = 0
    n = len(arr)
    swapped = True
    while (swapped != False):
        swapped = False
        cnt = cnt+1
        for i in range(n-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    
    return cnt


print(bubbleSort(arr))


