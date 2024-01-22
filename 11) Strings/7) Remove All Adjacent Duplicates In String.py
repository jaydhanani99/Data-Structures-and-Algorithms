# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, string: str) -> str:
        n = len(string)
        if n == 1:
            return string
        
        i = 0
        j = 0
        k = 1
        
        while k < n:
            # if k+1 == n and string[j] == string[k]:
            #     return string[0:i]
            while k+1 < n and string[j] == string[k]:
                k += 1
                # We would break here as we are removing adjacent only not all the repeatating elements
                break
            if j+1 != k:
                
                string = ''.join([string[0:i], string[k::]])
                n = len(string)
                # If adjacent found we would reset the i,j,k
                i = i-1 if i > 0 else 0
                j = i
                k = j + 1
            else:
                i += 1
                j += 1
                k += 1
                
        # To remove last two adjacent if any
        if i > 0 and string[i] == string[i-1]:
            return string[0:i-1]
        return string