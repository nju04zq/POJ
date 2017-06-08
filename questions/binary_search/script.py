# Find the target integer in an array sorted in non-descending order
# Return its index, if not exist, return -1
# Define the API interface as:
# def binary_search(target, array):

import sys
sys.path.append("../../")
import util.util as util

def brutal_search(target, array):
    for i, num in enumerate(array):
        if num == target:
            return i
    else:
        return -1

if __name__ == "__main__":
    def binary_search(target, array):
        return brutal_search(target, array)
else:
    def binary_search(target, array):
        return answer.binary_search(target, array)

def run_one_test_case():
    a = util.randint_list()
    t = util.randint()
    i = binary_search(t, a)
    j = brutal_search(t, a)
    if i == -1 and j != -1:
        test_case = "Find {0} in {1}, get {2}, could be {3}".format(\
                    t, a, i, j)
        return False, test_case
    elif i == -1 and j == -1:
        return True, ""
    elif i < 0 or i >= len(a):
        test_case = "Find {0} in {1}, get {2}, exceed limit".format(\
                    t, a, i)
        return False, test_case
    elif i != -1 and a[i] != t:
        test_case = "Find {0} in {1}, get {2}, but a[i] != t".format(\
                    t, a, i)
        return False, test_case
    else:
        return True, ""

def run_test():
    rc, passed, total, err = util.run_test_in_parallel(run_one_test_case, 10000)
    return rc, passed, total, err

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
