# https://www.interviewbit.com/problems/diffk/
# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, nums, k):
        n = len(nums)
        # if the question is to find the sum of two element = B
        # then we can easily use the two pointer start from 0 and n-1
        # However here we need to find the difference so we cannot determine the direction
        # based on the difference
        # if we want to use two pointer we need to use start from 0 and end from 1
        # and increament values of start or end depending on the differences
        # or else we can pick element one by one and do binary search to find the k+picked element in remaining array
        start = 0
        end = 1
        while start < n and end < n:
            current_diff = nums[end] - nums[start]
            if current_diff == k and start != end:
                return 1
            elif current_diff > k:
                # if we increase the start that means difference will be decreased
                start += 1
            else:
                # if we increase the end that means difference will be increased
                end += 1
        return 0