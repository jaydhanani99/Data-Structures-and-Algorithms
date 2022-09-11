# https://leetcode.com/problems/maximum-subarray/submissions/
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
# https://www.interviewbit.com/old/problems/max-sum-contiguous-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Editorial approach refer: https://www.youtube.com/watch?v=HCL4_bOd3-4
        max_sum = nums[0]
        current_sum = 0
        n = len(nums)
        for i in range(n):
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum
        
        # Another approach refer: https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
        # Assuming that first element is the subarray itself which sum is largest
        global_max = nums[0]
        local_max = 0
        n = len(nums)
        
        for i in range(n):
            # The maximum of current element of addition of the element to previous sum
            # This would be the useful when nums[i] and local_max both are negative
            local_max = max(nums[i], nums[i] + local_max)
            if local_max > global_max:
                global_max = local_max
                
        return global_max