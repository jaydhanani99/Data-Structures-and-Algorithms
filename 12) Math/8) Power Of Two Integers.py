# https://www.interviewbit.com/old/problems/power-of-two-integers/
# https://practice.geeksforgeeks.org/problems/check-if-a-number-can-be-expressed-as-xy1606/1

import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, num):
        # Here we are  trying to express the number A in form of x^y
        # Here in question mention that y > 1
        # so minimum power is 2
        # If we talk about power 2
        # x^2 = A
        # x   = root(A)
        # so we can conclude that x should be less than or equal to A.
        # Now if we repeatedly divide the A with power y and last if we get 1 that means we can express it as power of x^y
        # Also note that A > 0 so if we talk about 1 than ans is also 1
        if num == 1:
            return 1
        else:
            for i in range(2, int(math.sqrt(num))+1):
                inputNum    =   num
                while(inputNum%i == 0):
                    inputNum = int(inputNum//i)
                    if inputNum == 1:
                        return 1
            return 0