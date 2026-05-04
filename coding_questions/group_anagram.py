words = ["eat", "tea", "tan", "ate", "nat", "bat"]

from collections import defaultdict

def group_anagram(words):
  d = defaultdict(list)
  for word in words:
    key = tuple(sorted(word))
    d[key].append(word)
  return list(d.values())  

print(group_anagram(words))