# https://leetcode.com/problems/reverse-string/submissions/

class Solution:
    def reverseString(self, string: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(string) - 1
        # We take two pointer, one is from start and second is from end and replace the char
        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1