# https://leetcode.com/problems/3sum/submissions/

class Solution:
    def threeSum(self, nums):
        output = []
        
        n = len(nums)
        # Sorting the input array
        nums.sort()
        for i in range(n-2):
            # After considering first ith element skipping the same elements
            if i != 0 and nums[i-1] == nums[i]:
                continue
            start = i + 1
            end = n-1
            
            while start < end:
                current_sum = nums[i]+nums[start]+nums[end]
                if current_sum == 0:
                    output.append([nums[i], nums[start], nums[end]])
                    
                    # After considering this start and end, skipping the same elements
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    end -= 1
                elif current_sum > 0:
                    end -= 1
                else:
                    start += 1
                    
        return output
                
                