def binary_search_nearest(target, array):
    if len(array) == 0:
        return -1
    low, high= 0, len(array) - 1
    while True:
        mid = high - (high - low)/2
        if low == mid or high == mid:
            break
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid
        else:
            low = mid

    diff_low = abs(target - array[low])
    diff_high = abs(target - array[high])
    if diff_low == diff_high:
        return low
    elif diff_low < diff_high:
        return low
    else:
        return high
