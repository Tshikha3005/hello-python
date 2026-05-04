nums = [1,2,3,1]

def contain_dups(nums):
  seen = set()
  for i in nums:
    if i in seen:
     return True
    seen.add(nums[i])
  return False
  
print(contain_dups(nums))