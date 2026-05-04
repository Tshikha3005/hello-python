# Longest Consecutive Sequence
# [100,4,200,1,3,2]   # 4 (1,2,3,4)
# [0,3,7,2,5,8,4,6,0,1] # 9
# []                   
def longest_consecutive(nums):
    s = set(nums)
    longest = 0

    for n in s:
        if n-1 not in s:
            length = 1
            while n+length in s:
                length += 1
            longest = max(longest, length)

    return longest