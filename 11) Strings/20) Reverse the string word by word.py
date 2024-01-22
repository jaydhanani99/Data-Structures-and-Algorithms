# https://leetcode.com/problems/reverse-words-in-a-string
class Solution:
    def reverseWords(self, string: str) -> str:
        words = string.split()
        n = len(words)
        for i in range(n):
            words[i] = words[i].strip()
        return ' '.join(reversed(words))


# https://www.interviewbit.com/problems/reverse-the-string/
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, string):
        return ' '.join(reversed(string.split()))