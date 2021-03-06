# Give an array filled with integers, sort it in non-decending order,
# using insertion sort
# Define the API interface as:
# def insertion_sort(a):

import sys
sys.path.append("../../")
import util.randutil as randutil
import util.testutil as testutil

def python_sort(a):
    a.sort()

if __name__ == "__main__":
    def insertion_sort(a):
        python_sort(a)
else:
    def insertion_sort(a):
        return answer.insertion_sort(a)

def run_one_test_case(a):
    b = a[:]
    c = a[:]
    python_sort(b)
    insertion_sort(c)
    if b == c:
        return True, ""
    else:
        err = "Sort {0}, should be {1}, but got {2}".format(\
              a, b, c)
        return False, err

def generate_test_data():
    test_data_list = []
    for i in xrange(10000):
        a = randutil.randint_array()
        test_data_list.append(a)
    return test_data_list

def run_test():
    test_data_list = generate_test_data()
    result = testutil.run_test_in_parallel(run_one_test_case, test_data_list)
    rc, passed, total, fail_case = result
    return rc, passed, total, fail_case

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
