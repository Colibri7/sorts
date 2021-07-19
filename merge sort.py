def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0  # initial index of first subarray
    j = 0  # initial index of second subarray
    k = l  # initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # copy the remaining elements if L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy the remaining elements if R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1


# l is for left index and r is tiht index of the sub-arr of arr to be sorted

def mergeSort(arr, l, r):
    if l < r:
# same as (l+r)//2,but avoids overflow for large l and h
        m = (l+(r-1))//2

        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)


arr =  [12, 11, 13, 5, 6, 7]

n = len(arr)

print ("Given array is", arr)


mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i]),



