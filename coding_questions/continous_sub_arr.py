# Continuous Subarray Sum
# ([23,2,4,6,7], 6)   # True
# ([23,2,6,4,7], 13)  # False
# ([0,0], 0)          # True
def check_subarray(nums, k):
    mod_map = {0: -1}
    total = 0

    for i, n in enumerate(nums):
        total += n
        mod = total % k

        if mod in mod_map:
            if i - mod_map[mod] > 1:
                return True
        else:
            mod_map[mod] = i

    return False