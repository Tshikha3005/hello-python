nums = [1,1,2,2,3]

s= list(set(nums))
print(s)

# other way
def remove_dups(nums):
  seen = set()
  result = []
  for num in nums:
    if num not in seen:
      seen.add(num)
      result.append(num)
  return result

print(remove_dups([1,1,2,2,3]))