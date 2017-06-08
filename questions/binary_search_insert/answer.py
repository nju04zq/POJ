def binary_insert(target, array):
    if len(array) == 0:
        return 0
    low, high = 0, len(array)-1
    while True:
        mid = high - (high - low)/2
        if mid == low or mid == high:
            break
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if target <= array[low]:
        return low
    elif target <= array[high]:
        return high
    else:
        return high + 1
