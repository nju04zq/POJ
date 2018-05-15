# find sum of two numbers equals to a target int in a unsorted int array
# return all the unique int pairs
# for example, has [1, 2, 2, 3, 4], target 5,
# return [(1, 4), (2, 3)]
# use hash table to resolve
# Define the API interface as:
# def twoSum(nums, target):

import sys
sys.path.append("../../")
import util.randutil as randutil
import util.testutil as testutil

if __name__ == "__main__":
    def twoSum(nums, target):
        return twoSumBf(nums, target)
else:
    def twoSum(nums, target):
        return answer.twoSum(nums, target)

def twoSumBf(nums, target):
    results = []
    for i in xrange(len(nums)):
        for j in xrange(len(nums)):
            if i == j:
                continue
            elif nums[i] + nums[j] == target:
                if nums[i] < nums[j]:
                    results.append((nums[i], nums[j]))
                else:
                    results.append((nums[j], nums[i]))
    s = set()
    for t in results:
        s.add(t)
    results = []
    for t in s:
        results.append(t)
    return results

def verify_results(results, target):
    verified = []
    for t in results:
        if len(t) != 2:
            return "Get {0}, expect tuple with 2 numbers".format(t)
        if t[0] + t[1] != target:
            return "Get {0}, whose sum isn't {1}".format(t, target)
    return ""

def check_results_dup(results):
    unique = set()
    for t in results:
        if t[0] > t[1]:
            t = (t[1], t[0])
        if t not in unique:
            unique.add(t)
        else:
            return "Dup pair {0} found!".format(t)
    return ""

def check_missing_pair(res, ans):
    for t in ans:
        t1 = (t[1], t[0])
        if t not in res and t1 not in res:
            return "Missing {0}".format(t)
    return ""

def run_one_test_case(nums, target):
    test_case = "nums {0}, target {1}\n".format(nums, target)
    ans = twoSumBf(nums, target)
    res = twoSum(nums, target)
    ans_res = "get {0}, expect{1}\n".format(res, ans)
    err = verify_results(res, target)
    if err != "":
        return False, test_case + ans_res + err
    err = check_results_dup(res)
    if err != "":
        return False, test_case + ans_res + err
    err = check_missing_pair(res, ans)
    if err != "":
        return False, test_case + ans_res + err
    return True, ""

def generate_test_data():
    test_data_list = []
    for i in xrange(1000):
        nums = randutil.randint_array(min_int=-20, max_int=20)
        target = randutil.randint(min_int=-50, max_int=50)
        test_data_list.append((nums, target))
    return test_data_list

def run_test():
    test_data_list = generate_test_data()
    result = testutil.run_test_in_parallel(run_one_test_case, test_data_list)
    rc, passed, total, fail_case = result
    print fail_case
    return rc, passed, total, fail_case

if __name__ == "__main__":
    rc, passed, total, fail_case = run_test()
    print rc, passed, total, fail_case
