# https://leetcode.com/problems/sort-colors/
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
# https://www.interviewbit.com/old/problems/sort-by-color/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        low = 0
        i = 0
        high = n - 1
        # Using in-place modification
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
            if nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
                i -= 1
            i += 1
        return
        
        # Another approach using extra space
        total_zero = 0
        total_one = 0
        total_two = 0
        
        for x in nums:
            if x == 0:
                total_zero += 1
            if x == 1:
                total_one += 1
            if x == 2:
                total_two += 1
        for i in range(total_zero):
            nums[i] = 0
        for i in range(total_zero, total_zero+total_one):
            nums[i] = 1
        for i in range(total_zero+total_one, total_zero+total_one+total_two):
            nums[i] = 2