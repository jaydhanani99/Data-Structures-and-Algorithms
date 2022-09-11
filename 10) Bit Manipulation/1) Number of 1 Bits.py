# https://www.interviewbit.com/old/problems/number-of-1-bits/
# https://practice.geeksforgeeks.org/problems/set-bits0143/1
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, number):
        # number of 1 is also called has hamming weight
        count = 0
        while number > 0:
            # This would give the last digit of number
            if number&1 == 1:
                count += 1
            
            # Right shift the operator which shift one position and add 0 to front
            number >>= 1 # number = number >> 1
        return count