# Permutation in String
# ("ab", "eidbaooo")  # True
# ("ab", "eidboaoo")  # False
# ("a", "a")          # True
from collections import Counter

def check_perm(s1, s2):
    need = Counter(s1)
    window = Counter()

    left = 0

    for right in range(len(s2)):
        window[s2[right]] += 1

        if right - left + 1 > len(s1):
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1

        if window == need:
            return True

    return False