# Add two integers, return the sum
# Define the API interface as:
# def add(a, b):

import sys
sys.path.append("../../")
import util.util as util

if __name__ == "__main__":
    def add(a, b):
        return a + b
else:
    def add(a, b):
        return answer.add(a, b)

def run_one_test_case():
    a = util.randint()
    b = util.randint()
    c1 = a + b
    c2 = add(a, b)
    if c1 == c2:
        return True, ""
    else:
        test_case = "{0} + {1}, should be {2}, but got {3}".format(\
                    a, b, c1, c2)
        return False, test_case

def run_test():
    test_case_size = 100
    for i in xrange(test_case_size):
        rc, case_str = run_one_test_case()
        if rc == True:
            continue
        else:
            return False, i+1, test_case_size, case_str
    else:
        return True, test_case_size, test_case_size, ""

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
