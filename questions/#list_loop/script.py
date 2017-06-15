# 1. Check whether a list has loop, if yes, return the entry node for the loop,
# with id(node), otherwise, return None
# Define the API interface as:
# def get_list_loop_entry(a):
#
# 2. Calculate the loop size for a list, that is how many nodes in the loop,
# if there is no loop, return 0
# Define the API interface as:
# def get_list_loop_size(a):

import sys
sys.path.append("../../")
import util.util as util

def brutal_get_loop_entry_node(a):
    node_set = set()
    p = a
    while p is not None:
        if id(p) in node_set:
            return p
        else:
            node_set.add(id(p))
        p = p.next
    else:
        return None

def brutal_get_loop_entry(a):
    node = brutal_get_loop_entry_node(a)
    if node is None:
        return None
    else:
        return id(node)

def brutal_get_loop_size(a):
    entry_node= brutal_get_loop_entry_node(a)
    if entry_node is None:
        return 0
    loop_size = 0
    p = entry_node
    while True:
        loop_size += 1
        p = p.next
        if p is entry_node:
            break
    return loop_size

if __name__ == "__main__":
    def get_list_loop_entry(a):
        return brutal_get_loop_entry(a)
    def get_list_loop_size(a):
        return brutal_get_loop_size(a)
else:
    def get_list_loop_entry(a):
        return answer.get_list_loop_entry(a)
    def get_list_loop_size(a):
        return answer.get_list_loop_size(a)

def generate_test_data():
    test_data = []
    for i in xrange(1, 11):
        a = util.generate_list(size=i)
        test_data.append(util.copy_list(a))
        p = a
        a_tail = util.get_list_tail(a)
        while p is not None:
            a_tail.next = p
            test_data.append(util.copy_list(a))
            a_tail.next = None
            p = p.next
    return test_data

def run_one_test_case(a):
    e1 = brutal_get_loop_entry(a)
    e2 = get_list_loop_entry(a)
    if e1 != e2:
        err = "list {0}, loop entry should be {1}, get {2}".format(\
              util.dump_loop_list(a), e1, e2)
        return False, err 
    s1 = brutal_get_loop_size(a)
    s2 = get_list_loop_size(a)
    if s1 != s2:
        err = "list {0}, loop size should be {1}, get {2}".format(\
              util.dump_loop_list(a), s1, s2)
        return False, err
    return True, ""

def run_test():
    test_data_list = generate_test_data()
    result = util.run_test_in_parallel(run_one_test_case, test_data_list)
    rc, passed, total, fail_case = result
    return rc, passed, total, fail_case

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
