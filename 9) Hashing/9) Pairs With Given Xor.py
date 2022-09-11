# https://www.interviewbit.com/old/problems/pairs-with-given-xor/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, numbers, k):
        # Please note that A^B = C then B = A^C
        
        # Proof: 
        # a xor b = c
        # take xor with 'a' both side
        # a xor(a xor b) = a xor c
        # Now, we know a xor a = 0,
        # 0 xor b = a xor c
        # or, we can say: -
        # b = a xor c

        count = 0
        dict = {}
        for x in numbers:
            if x^k in dict:
                count += 1
            dict[x] = 1
        return count