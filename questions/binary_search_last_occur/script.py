# Find the target integer last occuring in an array,
# which is sorted in non-descending order
# Return its index, if not exist, return -1
# Define the API interface as:
# def binary_search_last_occur(target, array):

import sys
sys.path.append("../../")
import util.util as util

def brutal_search(target, array):
    i = len(array) - 1
    while i >= 0:
        if array[i] == target:
            return i
        i -= 1
    else:
        return -1

if __name__ == "__main__":
    def binary_search_last_occur(target, array):
        return brutal_search(target, array)
else:
    def binary_search_last_occur(target, array):
        return answer.binary_search_last_occur(target, array)

def run_one_test_case():
    a = util.randint_list()
    t = util.randint()
    i = binary_search_last_occur(t, a)
    j = brutal_search(t, a)
    if i != j:
        test_case = "Find first occur {0} in {1}, get {2}, should {3}".format(\
                    t, a, i, j)
        return False, test_case
    else:
        return True, ""

def run_test():
    rc, passed, total, err = util.run_test_in_parallel(run_one_test_case, 10000)
    return rc, passed, total, err

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
