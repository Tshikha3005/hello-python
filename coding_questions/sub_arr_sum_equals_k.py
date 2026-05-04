# Subarray Sum Equals K
# ([1,1,1], 2)       # 2
# ([1,2,3], 3)       # 2
# ([0,0,0], 0)       # 6
def subarray_sum(nums, k):
    count = {0:1}
    total = 0
    res = 0

    for n in nums:
        total += n
        if total - k in count:
            res += count[total - k]
        count[total] = count.get(total, 0) + 1

    return res