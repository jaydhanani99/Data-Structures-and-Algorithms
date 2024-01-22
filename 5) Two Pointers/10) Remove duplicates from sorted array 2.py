# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, nums):
        n = len(nums)
        new_count = 0
        i = 0
        while i < n:
            start_i = i
            # Skipping duplicate elements
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            if i != start_i:
                # Deleting repeating elements
                del nums[start_i: i-1]
                
                # Modify i and size of the array after deleting elements
                n -= i-start_i-1
                new_count += 1
            i = start_i+1
            new_count += 1
                
            
        return new_count