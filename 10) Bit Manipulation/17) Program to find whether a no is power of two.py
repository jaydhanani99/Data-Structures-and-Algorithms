# https://practice.geeksforgeeks.org/problems/power-of-2-1587115620/1
# https://leetcode.com/problems/power-of-two/submissions/

class Solution:
    def isPowerOfTwo(self, number: int) -> bool:
        # There are multiple approaches
        # 1) A simple method for this is to simply take the log of the number on base 2 and if you get an integer then the number is the power of 
        # 2) Another solution is to keep dividing the number by two, i.e, do n = n/2 iteratively
        # 3) All power of two numbers has only a one-bit set
#         count = 0
#         while number > 0:
#             # This would give the last digit of number
#             if number&1 == 1:
#                 count += 1
            
#             # Right shift the operator which shift one position and add 0 to front
#             number >>= 1 # number = number >> 1
#         # If only 1 bit set that means it's power of 2
#         return count == 1
        
        # 4) If we subtract a power of 2 numbers by 1 then all unset bits after the only set bit become set; and the set bit becomes unset.
        # So AND of number and number-1 would be zero
        return False if number == 0 or number&(number-1) != 0 else True