# https://www.interviewbit.com/old/problems/palindrome-integer/
# https://leetcode.com/problems/palindrome-number

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, x):
        x = str(x)
        
        return int(x == x[::-1])
        
        # Another approach
        if x < 0:
            return 0
            
        string = ""
        
        while x > 0:
            string += str(x%10)
            x //= 10
        return int(string == string[::-1])