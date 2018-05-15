def twoSum(nums, target):
    tbl = {}
    for num in nums:
        if num in tbl:
            tbl[num] += 1
        else:
            tbl[num] = 1
    results = []
    for num in nums:
        need = target - num
        if need not in tbl:
            continue
        tbl[num] -= 1
        if tbl[need] <= 0:
            tbl[num] += 1
        else:
            tbl[need], tbl[num] = 0, 0
            results.append((num, need))
    return results
