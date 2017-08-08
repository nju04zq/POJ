def binary_search_last_smaller(target, array):
    if len(array) == 0:
        return -1
    low, high = 0, len(array)-1
    while low < high:
        mid = high - (high-low)/2
        if array[mid] >= target:
            high = mid - 1
        else:
            low = mid
    if array[low] < target:
        return low
    else:
        return -1

