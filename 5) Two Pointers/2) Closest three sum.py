# https://www.interviewbit.com/problems/3-sum/
# https://leetcode.com/problems/3sum-closest/submissions/


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, nums, target):
        n = len(nums)
        
        # First we sort the array and then we use the three pointer approach
        nums.sort()
        # Here we use three pointers
        # first will traverse the array
        # second will point from the starting of the current array
        # third will point from the ending of the current array
        
        # Initially we assume that first three element will be closer
        # After traversing the array we update it if we found any closer which is less than the closest
        cloest_sum = nums[0]+nums[1]+nums[2]
        
        for i in range(0, n-2):
            start = i + 1
            end = n - 1
            while start < end:
                current_sum = nums[i]+nums[start]+nums[end]
                # We can say that this is the very closest which the same as B
                if current_sum == target:
                    return current_sum
                elif abs(current_sum - target) < abs(cloest_sum - target):
                    cloest_sum = current_sum
                
                # If current_sum is greater we decreament the end pointer to lower the current_sum
                if current_sum > target:
                    end -= 1
                # else we increament the start pointer to increase the current_sum
                else:
                    start += 1
        return cloest_sum