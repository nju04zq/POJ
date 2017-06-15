def selection_sort(a):
    if len(a) == 0:
        return
    for i in xrange(len(a)):
        min_idx, min_val = i, a[i]
        for j in xrange(i+1, len(a)):
            if a[j] < min_val:
                min_idx = j
                min_val = a[j]
        if i != min_idx:
            a[i], a[min_idx] = a[min_idx], a[i]
        print i, a
