def top_k(nums, k):
  count = {}
  for n in nums:
    count[n] = count.get(n, 0) + 1
# when you pass a dictionary into sorted() 
# count = {1:3, 2: 2, 3: 1}
# sorted(count) actually sort keys not values [1,2,3]
# key=count.get => this tells python sort keys actually based on their values in the dictionary
# sort by freq(Asc) [3,2,1]
# reverse true means descending
# [1,2,3]
# [:k] slice by k 
  return sorted(count, key=count.get, reverse=True)[:k]

print(top_k([1,1,1,2,2,3], 2))