# https://www.interviewbit.com/old/problems/pick-from-both-sides/
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, nums, k):
        if not nums:
            return 0
        n = len(nums)
        
        # The idea is to maintain two array 
        #  1) prefix_sum which stores the increamental sum of array
        #  2) suffix_sum which stores the increamental sum of array in reverse order
        # also we would store prefix sum for first k elements and suffix_sum for last k elemtns
        # e.g. for array [5, -2, 3 , 1, 2] and k = 3
            # prefix_sum would be [5, 3, 6]
            # suffix_sum would be [2, 3, 6]
            # now we start iterating from i
            # when i == 0:
                # 1 element from start and 2 elements from end
                # here we are taking 2 elements sum that we have taken index 1 in suffix_sum
                # which eventually prefix_sum[0] + suffix_sum[1]
                # which is prefix_sum[i] + suffix_sum[k-i-2] 
            
        
        
        prefix_sum = [nums[0]]
        suffix_sum = [nums[-1]]
        
        
        for i in range(1, k):
            prefix_sum.append(prefix_sum[-1]+nums[i])
            suffix_sum.append(suffix_sum[-1]+nums[n-i-1])
        
        # which is the sum of first k elements
        ans = prefix_sum[-1]
        for i in range(0, k-1):
            ans = max(ans, prefix_sum[i] + suffix_sum[k-i-2])
        # which is the maximum of calculated ans, sum of first k, sum of last k elements
        return max(ans, prefix_sum[-1], suffix_sum[-1])