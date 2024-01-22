# https://www.interviewbit.com/old/problems/min-steps-in-infinite-grid/
# https://www.geeksforgeeks.org/minimum-steps-needed-to-cover-a-sequence-of-points-on-an-infinite-grid/


import math
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        totalSteps  =   0
        # Here we calculate distance between two points.
        # Here we can increament or decreament the position of x and y
        # so for example if a = [-7, -13] and b = [1, -5]
        # we try to get closer to point b from point a by increamenting x only or y only or x and y both or decreamenting x only or y only or x and y both
        # So we can achieve this using maximum of absolute distance of two point
        # note: x,y to x+1, y or x,y to x+1, y+1 would take the same step
        for i in range(0, len(A)-1):
            totalSteps     +=      max(abs(A[i] - A[i+1]), abs(B[i] - B[i+1]))
        return totalSteps