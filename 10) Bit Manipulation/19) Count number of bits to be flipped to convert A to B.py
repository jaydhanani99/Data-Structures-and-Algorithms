# https://practice.geeksforgeeks.org/problems/bit-difference/0

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        # If we find the xor of two numbers that means we would have set bit in case of different bits in a and b
        # so we do xor of a and b and count the set bits in it
        number = a^b
        count = 0
        while number > 0:
            # This would give the last digit of number
            if number&1 == 1:
                count += 1
            
            # Right shift the operator which shift one position and add 0 to front
            number >>= 1 # number = number >> 1
        return count