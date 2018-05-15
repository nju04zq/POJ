def quick_sort(a):
    quick_sort_internal(a, 0, len(a))

def quick_sort_internal(a, low, high):
    if low >= high:
        return
    pos = split(a, low, high)
    quick_sort_internal(a, low, pos)
    quick_sort_internal(a, pos+1, high)

def split(a, low, high):
    pilot = a[low]
    j = low
    for i in xrange(low+1, high):
        if a[i] < pilot:
            a[j+1], a[i] = a[i], a[j+1]
            j += 1
    a[j], a[low] = a[low], a[j]
    return j
