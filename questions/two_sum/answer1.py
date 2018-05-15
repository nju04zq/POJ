def twoSum(nums, target):
    nums.sort()
    results = []
    i, j = 0, len(nums)-1
    while i < j:
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
            continue
        if j < (len(nums)-1) and nums[j] == nums[j+1]:
            j -= 1
            continue
        total = nums[i] + nums[j]
        if total < target:
            i += 1
        elif total > target:
            j -= 1
        else:
            results.append((nums[i], nums[j]))
            i += 1
            j -= 1
    return results
