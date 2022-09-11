# https://practice.geeksforgeeks.org/problems/count-distinct-pairs-with-difference-k1233/1
# https://leetcode.com/problems/k-diff-pairs-in-an-array/


class Solution:
    def findPairs(self, nums, k):
        # Using two pointer
        start = 0
        end = 1
        n = len(nums)
        count = 0
        nums.sort()
        
        while start < n and end < n:
            current_diff = nums[end]-nums[start]
    
            if current_diff == k:
                count += 1
                # Skipping the same elements both the side
                while start < n-1 and nums[start] == nums[start+1]:
                    start += 1
                while end < n-1 and nums[end] == nums[end+1]:
                    end += 1
                
                # Increamenting start and end both
                start += 1
                end += 1
            elif current_diff > k:
                start += 1
            else:
                end += 1
            # Resetting the end in case of any
            if end <= start:
                end = start + 1
        return count
    
        # Using Binary Search
#         n = len(nums)
#         i = 0
#         count = 0
#         nums.sort()
#         while i < n:
#             low = i+1
#             high = n-1
#             while low <= high:
#                 mid = low + (high-low)//2
                
#                 if nums[mid] == k + nums[i]:
#                     count += 1
#                     break
#                 elif nums[mid] < k + nums[i]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#             # Skipping the same elements
#             while i < n - 1 and nums[i] == nums[i+1]:
#                 i += 1
#             i += 1
#         return count