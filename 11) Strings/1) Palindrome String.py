# https://www.interviewbit.com/old/problems/palindrome-string/
# https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, string):
        n = len(string)
        start = 0
        end = n-1
        while start < end:
            while start < end and not string[start].isalnum():
                start += 1
            while start < end and not string[end].isalnum():
                end -= 1
            if string[start].lower() != string[end].lower():
                return 0
            start += 1
            end -= 1
        return 1