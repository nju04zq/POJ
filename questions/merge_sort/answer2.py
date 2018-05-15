def merge_sort(a):
    tmp = a[:]
    step = 1
    while step < len(a):
        for start in xrange(0, len(a), 2*step):
            mid = start + step
            if mid >= len(a):
                continue
            end = mid + step
            if end >= len(a):
                end = len(a)
            merge(a, tmp, start, mid, end)
        step *= 2

def merge(a, tmp, start, mid, end):
    i, j, k = start, mid, 0
    while i < mid and j < end:
        if a[i] <= a[j]:
            tmp[k] =  a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1
    while i < mid:
        tmp[k] = a[i]
        i += 1
        k += 1
    while j < end:
        tmp[k] = a[j]
        j += 1
        k += 1
    for i in xrange(0, k):
        a[start+i] = tmp[i]
