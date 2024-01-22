# https://leetcode.com/problems/valid-anagram/submissions/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using sorting
        return ''.join(sorted(s)) == ''.join(sorted(t))
    
    
        # Without using sorting
        dict1 = {}
        dict2 = {}
        n = len(s)
        if n != len(t):
            return False
        
        for i in range(n):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
            
            if t[i] not in dict2:
                dict2[t[i]] = 1
            else:
                dict2[t[i]] += 1
        for i in dict1:
            if i not in dict2 or dict1[i] != dict2[i]:
                return False
        return True