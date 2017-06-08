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

def run_one_test_case():
    target = util.randint()
    array = util.randint_list()
    r1 = brutal_insert(target, array)
    r2 = binary_insert(target, array)
    if r1 == r2:
        return True, ""
    else:
        err = "Insert {0} in {1}, should be {3}, get {4}".format(\
              target, array, r1, r2)
        return False, err

def run_test():
    return util.run_test_in_parallel(run_one_test_case, 10000)

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
