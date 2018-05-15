def bubble_sort(a):
    if len(a) == 0:
        return
    i = len(a) - 1
    while i >= 0:
        for j in xrange(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        i -= 1
