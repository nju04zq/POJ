# Add two integers, return the sum
# Define the API interface as:
# def add(a, b):

import sys
sys.path.append("../../")
import util.randutil as randutil
import util.testutil as testutil

if __name__ == "__main__":
    def add(a, b):
        return a + b
else:
    def add(a, b):
        return answer.add(a, b)

def run_one_test_case(a, b):
    c1 = a + b
    c2 = add(a, b)
    if c1 == c2:
        return True, ""
    else:
        err = "{0} + {1}, should be {2}, but got {3}".format(\
              a, b, c1, c2)
        return False, err

def generate_test_data():
    test_data_list = []
    for i in xrange(100):
        a = randutil.randint()
        b = randutil.randint()
        test_data_list.append((a, b))
    return test_data_list

def run_test():
    test_data_list = generate_test_data()
    result = testutil.run_test_in_parallel(run_one_test_case, test_data_list)
    rc, passed, total, fail_case = result
    return rc, passed, total, fail_case

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
