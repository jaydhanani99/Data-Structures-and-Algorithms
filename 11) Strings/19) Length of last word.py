# https://www.interviewbit.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, string: str) -> int:
        words = string.split()
        if len(words) > 0:
            return len(words[-1])
        return 0