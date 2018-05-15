def smallest(a):
    if len(a) < 2:
        return None
    min1, min2 = min(a[0], a[1]), max(a[0], a[1])
    for i in xrange(2, len(a)):
        if a[i] < min1:
            min2 = min1
            min1 = a[i]
        elif a[i] < min2:
            min2 = a[i]
    return (min1, min2)
