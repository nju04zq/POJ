def upperbound(t, a):
    low, high = 0, len(a)-1
    while low < high:
        mid = low + (high-low)/2
        if a[mid] <= t:
            low = mid+1
        else:
            high = mid
    if low > high or a[low] <= t:
        return -1
    else:
        return low
