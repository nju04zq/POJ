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

def run_one_test_case():
    a = util.randint_list()
    t = util.randint()
    i = binary_search_nearest(t, a)
    j = brutal_search(t, a)
    if i < 0 and i == j:
        return True, ""
    if i < 0 or i >= len(a):
        test_case = "Find nearest {0} in {1}, get {2}, out of range".\
                    format(t, a, i)
        return False, test_case
    elif a[i] != a[j]:
        test_case = "Find nearest {0} in {1}, get {2}/{3}, should be {4}/{5}".\
                    format(t, a, i, a[i], j, a[j])
        return False, test_case
    else:
        return True, ""

def run_test():
    rc, passed, total, err = util.run_test_in_parallel(run_one_test_case, 10000)
    return rc, passed, total, err

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
