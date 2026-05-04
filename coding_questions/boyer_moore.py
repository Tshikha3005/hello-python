# Finding a Majority Element (one that appears more than \(n/2\) times) is commonly solved using two Python approaches: a Dictionary-based method for simplicity and the Boyer-Moore Voting Algorithm for optimal space efficiency.

nums = [3,3,4,2,3,3]

def majority(nums):
  count = {}
  for n in nums:
    count[n] = count.get(n,0) + 1
    print(count[n],len(nums)//2)
    if count[n] > len(nums)//2:
      return n
    
print(majority(nums))