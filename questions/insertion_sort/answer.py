def insertion_sort(a):
    if len(a) == 0:
        return
    for i in xrange(1, len(a)):
        j = i
        while j > 0:
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
            j -= 1
