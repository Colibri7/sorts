def quick_sort(arr):
    length = len(arr)

    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
        item_greater = []
        item_lower = []
        for item in arr:
            if item > pivot:
                item_greater.append(item)
            else:
                item_lower.append(item)
    return quick_sort(item_lower) + [pivot] + quick_sort(item_greater)


print(quick_sort([1, 10, 100, 4, 5, 3, 5, 46, 56, 547]))
