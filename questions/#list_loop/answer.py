def get_list_loop_entry_node(a):
    p1 = p2 = a
    # should choose p2_prev, instead of p1_prev
    # because p1_prev could be out of loop
    p2_prev = None
    while True:
        p1 = p1.next
        p2 = p2.next
        if p2 is None:
            return None
        p2_prev = p2
        p2 = p2.next
        if p2 is None:
            return None
        if p1 is p2:
            break
    p2_prev.next = None
    node = get_list_interection_node(a, p2)
    p2_prev.next = p2
    return node

def get_list_interection_node(a, b):
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
    return pa

def get_list_loop_entry(a):
    node = get_list_loop_entry_node(a)
    if node is not None:
        return id(node)
    else:
        return None

def get_list_loop_size(a):
    entry_node = get_list_loop_entry_node(a)
    if entry_node is None:
        return 0
    p = entry_node
    loop_size = 0
    while True:
        loop_size += 1
        p = p.next
        if p is entry_node:
            break
    return loop_size
