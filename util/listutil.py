class ListNode(object):
    def __init__(self, data=0):
        self.data = data
        self.next = None

def generate_list(size=None):
    if size is None:
        size = randint(min_int=1, max_int=10)
    head, prev = None, None
    for i in xrange(size):
        node = ListNode()
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
        prev = node
    return head

def append_list(head, node):
    if head is None:
        head = node
        return
    p = head
    while p is not None:
        prev = p
        p = p.next
    prev.next = node

def remove_list_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    p = head
    while p.next is not None:
        prev = p
        p = p.next
    prev.next = None
    return head

def get_list_tail(head):
    if head is None:
        return None
    p = head
    while p is not None:
        prev = p
        p = p.next
    return prev

def get_list_size(head):
    p, size = head, 0
    while p is not None:
        size += 1
        p = p.next
    return size

def dump_list(head):
    if head is None:
        return "None"
    p, s = head, ""
    while p is not None:
        if p.next is not None:
            s += "{0} -> ".format(id(p))
        else:
            s += "{0}".format(id(p))
        p = p.next
    return s

def copy_list(a):
    node_map = {}
    a1 = None
    p, prev = a, None
    while p is not None:
        if id(p) in node_map:
            prev.next = node_map[id(p)]
            break
        node = ListNode(p.data)
        if a1 is None:
            a1 = node
        if prev is not None:
            prev.next = node
        node_map[id(p)] = node
        prev = node
        p = p.next
    return a1

def dump_loop_list(a):
    node_set = set()
    p, s = a, ""
    while p is not None:
        if id(p) in node_set:
            s += " -> {0}".format(id(p))
            break
        node_set.add(id(p)) 
        if p is a:
            s += str(id(p))
        else:
            s += " -> {0}".format(id(p))
        p = p.next
    return s

def copy_list_pair(a, b):
    node_map = {}
    a1, b1 = None, None
    p, prev = a, None
    while p is not None:
        node = ListNode(p.data)
        node_map[id(p)] = node
        if a1 is None:
            a1 = node
        if prev is not None:
            prev.next = node
        prev = node
        p = p.next
    p, prev = b, None
    while p is not None:
        if id(p) in node_map:
            node = node_map[id(p)]
        else:
            node = ListNode(p.data)
        if b1 is None:
            b1 = node
        if prev is not None:
            prev.next = node
        prev = node
        p = p.next
    return a1, b1
