# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, string: str, k: int) -> str:
        i = 0
        n = len(string)
        while i < n:
            # left part of the string + reversed string of k char + right part of the string
            string = ''.join([string[0:i], ''.join(reversed(string[i:i+k])), string[i+k:]])
            i += 2*k
        return string