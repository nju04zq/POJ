# Give an unordered int array, return the smallest and the second smallest,
# the return value could be list or tuple, but should with the smallest as
# the first element
# Define the API interface as:
# def smallest(a):

import sys
sys.path.append("../../")
import util.randutil as randutil
import util.testutil as testutil

def brutal(a):
    if len(a) < 2:
        return None
    else:
        b = sorted(a)
        return (b[0], b[1])

if __name__ == "__main__":
    def smallest(a):
        return brutal(a)
else:
    def smallest(a):
        return answer.smallest(a)

def run_one_test_case(a):
    ans = brutal(a)
    res = smallest(a)
    if ans is None:
        if res is not None:
            return False, "Should return None for {0}".format(a)
        else:
            return True, ""
    elif res is None or len(res) != len(ans) or \
         res[0] != ans[0] or res[1] != ans[1]:
        return False, "Should return {0} for {1}, but get {2}".format(\
            ans, a, res)
    else:
        return True, ""

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
