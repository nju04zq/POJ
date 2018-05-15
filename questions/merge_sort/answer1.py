def merge_sort_internal(a, tmp, start, end):
    if (start + 1) >= end:
        return
    mid = end - (end - start)/2
    merge_sort_internal(a, tmp, start, mid)
    merge_sort_internal(a, tmp, mid, end)
    i, j, k = start, mid, 0
    while i < mid and j < end:
        if a[i] <= a[j]:
            tmp[k] = a[i]
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

def merge_sort(a):
    tmp = a[:]
    merge_sort_internal(a, tmp, 0, len(a))
