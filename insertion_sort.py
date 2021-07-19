def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


s = [5, 6, 8, 5, 3, 2, 4, 6, 7, 8, 434, 45456, 123, 646]
insertion_sort(s)
print(s)