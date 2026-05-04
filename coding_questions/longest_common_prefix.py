# Longest Common Prefix
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

def longestCommonPrefix(strs):
  # prefix = strs[0]
  # print(prefix, strs[1:])
  # for s in strs[1:]:
  #   print(s,s.startswith(prefix))
  #   while not s.startswith(prefix):
  #       print(prefix)
  #       prefix = prefix[:-1]
  #       print(prefix)
  #       if not prefix:
  #         return ""
  # return prefix
    if not strs:
        return ""
    
    # zip(*strs) takes ['flower', 'flow', 'flight'] and 
    # creates groups like: ('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i')...
    for i, characters in enumerate(zip(*strs)):
        # If the set has more than 1 character, the prefix has ended
        print(i,'i', characters,'characs', set(characters))
        if len(set(characters)) > 1:
            return strs[0][:i]
            
    # If the loop finishes, the shortest string is the prefix
    return min(strs, key=len)

# Example 1:
print(longestCommonPrefix(["flower", "flow", "flight"])) # "fl"