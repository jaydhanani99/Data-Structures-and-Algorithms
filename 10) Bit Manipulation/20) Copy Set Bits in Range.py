# https://practice.geeksforgeeks.org/problems/copy-set-bits-in-range0623/1#

class Solution:
    def setSetBit(self, x, y, l, r):
        # First approach is to compare the bit one by one and set the bit of x if it's in range l and r and in y bit is set
        
        # Other option is we would generate the number with number of set LSB bits is equals to the r-l+1
        n = r-l+1
        number = 0
        while n > 0:
            n-= 1
            number <<= 1
            number |= 1
        # We can do above step by number = (1<<(r-l+1)) - 1
        # e.g. x = 44, y = 3, l = 5 and r = 1
        # so y = 0000000....11
        # now if we do left shift 1 by (r-l+1) = 00..100000
        # and if we subtract 1 from it then it would be 000...11111 which is the same as above loop
        
        
        # After that we left shift it till l-1 to match set bits with y
        number = number << l-1
        # After that we do and operation with y so we would recieve set bits of y and all other bits except in range l and r would be 0
        # After that we do or operation with x 
        return x|(number&y)