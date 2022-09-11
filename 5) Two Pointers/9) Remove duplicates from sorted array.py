# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def findLastIndexOfRepeatingElement(self, nums, i, n):
        low = i
        high = n-1
        last_index = i
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == nums[i]:
                last_index = mid
                # Searching for right part to get repeating element
                low = mid+1
            elif nums[mid] > nums[i]:
                high = mid-1
            else:
                low = mid+1
        return last_index
    def removeDuplicates(self, nums):
        n = len(nums)
        new_count = 0
        i = 0
        while i < n:
            start_i = i
            # Skipping duplicate elements
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
                
            # Deleting repeating elements
            del nums[start_i: i]
            
            # Modify i and size of the array after deleting elements
            n -= i-start_i
            i = start_i+1
            new_count += 1
            
        return new_count
    
        # Using binary search to find repeating elementn = len(nums)
        # new_count = 0
        # i = 0
        # while i < n:
        #     start_i = i
        #     last_index = self.findLastIndexOfRepeatingElement(nums, i, n)
        #     # Deleting repeating elements
        #     del nums[start_i: last_index]
            
        #     # Modify i and size of the array after deleting elements
        #     n -= last_index-start_i
        #     i = start_i+1
        #     new_count += 1
        # return new_count