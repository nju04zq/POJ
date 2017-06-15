# Given a list with integers sorted in non-descending order, and a target int,
# return the first position where it could be inserted.
# For example, given [1, 3, 3], 0 could be inserted at 0, 2 at 1, 3 at 1, 4 at 3
# Define the API interface as:
# def binary_insert(target, array):

import sys
sys.path.append("../../")
import util.util as util

def brutal_insert(target, array):
    for i, num in enumerate(array):
        if num >= target:
            return i
    else:
        return len(array)

if __name__ == "__main__":
    def binary_insert(target, array):
        return brutal_insert(target, array)
else:
    def binary_insert(target, array):
        return answer.binary_insert(target, array)

def run_one_test_case(target, array):
    r1 = brutal_insert(target, array)
    r2 = binary_insert(target, array)
    if r1 == r2:
        return True, ""
    else:
        err = "Insert {0} in {1}, should be {3}, get {4}".format(\
              target, array, r1, r2)
        return False, err

def generate_test_data():
    test_data_list = []
    for i in xrange(10000):
        target = util.randint()
        array = util.randint_sorted_array()
        test_data_list.append((target, array))
    return test_data_list

def run_test():
    test_data_list = generate_test_data()
    result = util.run_test_in_parallel(run_one_test_case, test_data_list)
    rc, passed, total, fail_case = result
    return rc, passed, total, fail_case

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
