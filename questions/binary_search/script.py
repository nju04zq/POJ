# Find the target integer in an array sorted in non-descending order
# Return its index, if not exist, return -1
# Define the API interface as:
# def binary_search(target, array):

import sys
sys.path.append("../../")
import util.randutil as randutil
import util.testutil as testutil

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

def run_one_test_case(t, a):
    i = binary_search(t, a)
    j = brutal_search(t, a)
    if i == -1 and j != -1:
        err = "Find {0} in {1}, get {2}, should be {3}".format(\
              t, a, i, j)
        return False, err
    elif i == -1 and j == -1:
        return True, ""
    elif i < 0 or i >= len(a):
        err = "Find {0} in {1}, get {2}, exceed limit".format(\
              t, a, i)
        return False, err
    elif i != -1 and a[i] != t:
        err = "Find {0} in {1}, get {2}, but a[i] != t".format(\
              t, a, i)
        return False, err
    else:
        return True, ""

def generate_test_data_list():
    test_data_list = []
    for i in xrange(10000):
        t = randutil.randint()
        a = randutil.randint_sorted_array()
        test_data_list.append((t, a))
    return test_data_list

def run_test():
    test_data_list = generate_test_data_list()
    result = testutil.run_test_in_parallel(run_one_test_case, test_data_list)
    rc, passed, total, err = result
    return rc, passed, total, err

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
