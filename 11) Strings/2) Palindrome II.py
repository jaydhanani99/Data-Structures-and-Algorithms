# https://leetcode.com/problems/valid-palindrome-ii/submissions/

class Solution:
    def checkPalindrome(self, string):
        return True if string == string[::-1] else False
    
    def validPalindrome(self, string: str) -> bool:
        start = 0
        end = len(string)-1
        no_of_deleted_element = 0
        while start < end:
            if string[start] != string[end]:
                # If one char is mismatch we check for palindrome by incrementing start or decrementing end
                return self.checkPalindrome(string[start:end]) or self.checkPalindrome(string[start+1:end+1])
            start += 1
            end -= 1
        return True
            