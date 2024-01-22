#Reference:  https://www.youtube.com/watch?v=JUzYl1TYMcU

# https://www.interviewbit.com/old/problems/greatest-common-divisor/


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    # Here we can use modulo operation in euclidean algorithm
    def gcd(self, A, B):
        if A == 0:
            return B
        return self.gcd(B%A, A)