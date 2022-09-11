# https://www.interviewbit.com/old/problems/distribute-in-circle/

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, items, size, start_position):
        return (items+start_position-1)%size