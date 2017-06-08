def binary_search_last_occur(target, array):
    last_occur = -1
    low, high= 0, len(array) - 1
    while low <= high:
        mid = high - (high - low)/2
        if array[mid] == target:
            last_occur = mid
            low = mid + 1
        elif array[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    return last_occur

