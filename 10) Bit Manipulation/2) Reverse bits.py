# https://www.interviewbit.com/old/problems/reverse-bits/
# https://leetcode.com/problems/reverse-bits/submissions/

class Solution:
    def reverseBits(self, number: int) -> int:
        # Let's take intially reverse number as 0
        # now we take A & 1 so that we get the last digit of A
        # if last digit is 1 we need to set first digit of rev to 1 
        # However we currently set the last digit of rev and then we left shift it by 1 position so at last first digit will become the last and so on.
        # To set the last digit of rev 1 we simply do OR operation with 1.
        # if last digit is 0 then we do only left shift as we have taken rev as 0
        output = 0
        
        for i in range(32):
            if number & 1 == 1:
                output |= 1
            output <<= 1
            number >>= 1
        # At last we right shift output once as in last iteration we have left shifted one extra time
        # Other options is that we first left shift the bit then set the last shift
        output >>= 1
        return output