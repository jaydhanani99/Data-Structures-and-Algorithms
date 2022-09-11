# https://www.interviewbit.com/old/problems/total-moves-for-bishop/

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # left_bottom + left_top + right_bottom + right_top
        return min((8-A), (B-1))+min((A-1), (B-1))+min((A-1), (8-B))+min((8-A), (8-B))