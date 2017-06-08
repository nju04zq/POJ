# Check whether two list have intersection
# if yes, return the id for intersection node, id(node)
# otherwise, return None
# The two lists are guaranteed not empty
# Define the API interface as:
# def check_list_intersection(a, b):
# a/b are two lists, with list node defined as,
# class ListNode(object):
#     def __init__(self):
#         self.data = 0
#         self.next = None

import sys
sys.path.append("../../")
import util.util as util

def brutal_check(a, b):
    node_id_set = set()
    p = a
    while p is not None:
        node_id_set.add(id(p))
        p = p.next
    p = b
    while p is not None:
        if id(p) in node_id_set:
            return id(p)
        p = p.next
    else:
        return None

if __name__ == "__main__":
    def check_list_intersection(a, b):
        return brutal_check(a, b)
else:
    def check_list_intersection(a, b):
        return answer.check_list_intersection(a, b)

def run_one_test_case(a, b):
    r1 = brutal_check(a, b)
    r2 = check_list_intersection(a, b)
    if r1 == r2:
        return True, ""
    else:
        err = "For list a {0}, list b {1}, should be {2}, get {3}".format(\
              util.dump_list(a), util.dump_list(b), r1, r2)
        return False, err

def generate_test_data():
    test_data = []
    a = util.generate_list(1)
    b = util.generate_list(1)
    test_data.append(util.copy_list_pair(a, b))
    test_data.append(util.copy_list_pair(a, a))
    for i in xrange(100):
        a = util.generate_list()
        b = util.generate_list()
        test_data.append(util.copy_list_pair(a, b))
        test_data.append(util.copy_list_pair(a, a))
        p = a
        b_tail = util.get_list_tail(b)
        while p is not None:
            util.append_list(b, p)
            test_data.append(util.copy_list_pair(a, b))
            b_tail.next = None
            p = p.next
    return test_data

def run_test():
    test_data = generate_test_data()
    test_data_size = len(test_data)
    passed = 0
    for i, data_entry in enumerate(test_data):
        rc, err = run_one_test_case(*data_entry)
        if rc == False:
            return False, passed, test_data_size, err
        else:
            passed += 1
    return True, passed, passed, ""

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
