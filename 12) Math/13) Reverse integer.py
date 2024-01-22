# https://www.interviewbit.com/old/problems/reverse-integer/
# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        sign = True if x < 0 else False
        
        x = int(str(abs(x))[::-1])
        
        if x > 2**31 -1:
            return 0
        
        return -x if sign else x
    
    
        # Another approach
        ans   =   0
        sign    =   False
        if(x < 0):
            x   =   abs(x)
            sign    =   True
            # 32 big positive hex & num < 32 bit positive hex gives 32 big positive hex else it gives 0
        while(x > 0):
            ans = ans + x%10
            ans = ans*10
            x = int(x/10)
        ans = int(ans/10)
        
        if ans > 2**31 -1:
            return 0
        return -ans if sign else ans
    