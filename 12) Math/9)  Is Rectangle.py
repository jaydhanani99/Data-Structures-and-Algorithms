# https://www.interviewbit.com/old/problems/is-rectangle/

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        list = [A, B, C, D]
        list.sort()
        return int(list[0] == list[1] and list[2] == list[3])