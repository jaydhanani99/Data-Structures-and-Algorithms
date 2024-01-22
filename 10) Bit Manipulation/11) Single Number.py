# https://www.interviewbit.com/problems/single-number/
# https://leetcode.com/problems/single-number/submissions/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, number):
        # XOR of the same value is zero
        # So we xor every elements and return the result
        n = len(number)
        ans = number[0]
        for i in range(1, n):
            ans ^= number[i]
        return ans
        