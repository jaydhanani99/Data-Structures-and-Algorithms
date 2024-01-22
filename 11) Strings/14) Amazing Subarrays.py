# https://www.interviewbit.com/old/problems/amazing-subarrays/

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, string):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        ans = 0
        for i in range(len(string)):
            if string[i] in vowels:
              ans = ans + (len(string) - i)%10003
        return ans%10003