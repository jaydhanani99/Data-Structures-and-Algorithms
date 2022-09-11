# https://leetcode.com/problems/rotate-array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        
        # First approach
        while k > 0:
            k -= 1
            nums.insert(0, nums.pop())
        return nums
        
        # Another simple approach
        nums[::] = nums[(n-k)::]+nums[:n-k]
            
        