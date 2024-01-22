# https://www.interviewbit.com/old/problems/compare-version-numbers/
# https://leetcode.com/problems/compare-version-numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        value1 = 0
        value2 = 0
        
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        # Removing the trailing zeros from both the arrays
        n1 = len(version1)
        while n1 > 0 and int(version1[n1-1]) == 0:
            version1.pop()
            n1 -= 1
            
        n2 = len(version2)
        while n2 > 0 and int(version2[n2-1]) == 0:
            version2.pop()
            n2 -= 1
        
        i = 0
        j = 0
        # Comparing the version one by one from left to right
        n = min(n1, n2)
        while i < n:
            if int(version1[i]) > int(version2[i]):
                return 1
            if int(version1[i]) < int(version2[i]):
                return -1
            i += 1
            j += 1
        
        # if we reach at the end of the both version that means both are same
        if i == n1 and j == n2:
            return 0
        # if we reach at version1 that means version2 is greater than the version1
        if i == n1:
            return -1
        return 1