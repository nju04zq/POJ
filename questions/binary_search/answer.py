def binary_search(target, array):
    low, high= 0, len(array) - 1
    while low <= high:
        mid = high - (high - low)/2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    else:
        return -1

