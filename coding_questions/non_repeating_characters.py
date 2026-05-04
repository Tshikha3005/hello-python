# First Non-Repeating Character (DICT)
s = "aabbcde"

def first_nonrepeat(s):
  count = {}
  for ch in s:
    count[ch] = count.get(ch,0) + 1

  for ch in s:
    if count[ch] == 1:
      return ch
    

print(first_nonrepeat("aabbcde"))