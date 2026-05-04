# Minimum Window Substring 💀
# ("ADOBECODEBANC", "ABC")  # "BANC"
# ("a", "a")                # "a"
# ("a", "aa")               # ""
from collections import Counter

def min_win(s, t):
  need = Counter(t)
  have = {}
  left = 0
  res = ''

  required = len(need)
  formed = 0
  for right in range(len(s)):
    c = s[right]
    have[c] = have.get(c,0) + 1
    if c in need and have[c] == need[c]:
      formed +=1
    while formed == required:  
      if not res or (right - left + 1) < len(s):
        res = s[left: right+1]
      have[s[left]] -= 1
      if s[left] in need and have[s[left]] < need[s[left]]:
        formed -= 1
      left += 1

    return res