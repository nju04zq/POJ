def check_list_intersection(a, b):
    pa, pb = a, b
    while pa is not pb:
        if pa is None:
            pa = b
        else:
            pa = pa.next
        if pb is None:
            pb = a
        else:
            pb = pb.next
    if pa is None:
        return None
    else:
        return id(pa)
