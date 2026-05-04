# Product of Array Except Self
# [1,2,3,4]     # [24,12,8,6]
# [-1,1,0,-3,3] # [0,0,9,0,0]
# [1,0]         # [0,1]

def product(nums):
    n = len(nums)
    res = [1]*n
    print(res)
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
        print(res, left, i , res[i], nums[i])
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
        # print(right, res)
    return res

print(product([1,2,3,4]))