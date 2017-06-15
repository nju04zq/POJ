# Find the integer which has value nearest with target's, 
# in an array sorted in non-descending order, return its index
# if there are two different, return the small one's index
# Define the API interface as:
# def binary_search_nearest(target, array):

import sys
sys.path.append("../../")
import util.util as util

def brutal_search(target, array):
    min_idx, min_diff = -1, None
    for i, num in enumerate(array):
        diff = abs(num -target)
        if min_diff is None or diff < min_diff:
            min_idx, min_diff = i, diff
    return min_idx

if __name__ == "__main__":
    def binary_search_nearest(target, array):
        return brutal_search(target, array)
else:
    def binary_search_nearest(target, array):
        return answer.binary_search_nearest(target, array)

def run_one_test_case(t, a):
    i = binary_search_nearest(t, a)
    j = brutal_search(t, a)
    if i < 0 and i == j:
        return True, ""
    if i < 0 or i >= len(a):
        err = "Find nearest {0} in {1}, get {2}, out of range".\
              format(t, a, i)
        return False, err
    elif a[i] != a[j]:
        err  = "Find nearest {0} in {1}, get {2}/{3}, should be {4}/{5}".\
               format(t, a, i, a[i], j, a[j])
        return False, err
    else:
        return True, ""

def generate_test_data_list():
    test_data_list = []
    for i in xrange(10000):
        t = util.randint()
        a = util.randint_sorted_array()
        test_data_list.append((t, a))
    return test_data_list

def run_test():
    test_data_list = generate_test_data_list()
    result = util.run_test_in_parallel(run_one_test_case, test_data_list)
    rc, passed, total, err = result
    return rc, passed, total, err

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
