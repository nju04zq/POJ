def binary_search_first_larger(target, array):
    if len(array) == 0:
        return -1
    low, high = 0, len(array)-1
    while low < high:
        mid = high - (high-low)/2
        if mid == high:
            break
        if array[mid] <= target:
            low = mid + 1
        else:
            high = mid
    if array[low] > target:
        return low 
    elif array[high] > target:
        return high
    else:
        return -1

