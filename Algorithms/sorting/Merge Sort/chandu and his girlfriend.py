# Write your code here
def dualPivotQuickSort(arr, low, high):
     
    if low < high:
         
        # lp means left pivot and rp  
        # means right pivot
        lp, rp = partition(arr, low, high)
         
        dualPivotQuickSort(arr, low, lp - 1)
        dualPivotQuickSort(arr, lp + 1, rp - 1)
        dualPivotQuickSort(arr, rp + 1, high)
         
def partition(arr, low, high):
     
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
         
    # p is the left pivot, and q is the right pivot.
    j = k = low + 1
    g, p, q = high - 1, arr[low], arr[high]
     
    while k <= g:
         
        # If elements are less than the left pivot
        if arr[k] < p:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1
             
        # If elements are greater than or equal  
        # to the right pivot
        elif arr[k] >= q:
            while arr[g] > q and k < g:
                g -= 1
                 
            arr[k], arr[g] = arr[g], arr[k]
            g -= 1
             
            if arr[k] < p:
                arr[k], arr[j] = arr[j], arr[k]
                j += 1
                 
        k += 1
         
    j -= 1
    g += 1
     
    # Bring pivots to their appropriate positions.
    arr[low], arr[j] = arr[j], arr[low]
    arr[high], arr[g] = arr[g], arr[high]
     
    # Returning the indices of the pivots
    return j, g

           

for t in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split(" ")]
   
    dualPivotQuickSort(arr, 0, n-1)
    for i in range(n-1, -1, -1):
        print(arr[i], end=" ")

    print("\n")
