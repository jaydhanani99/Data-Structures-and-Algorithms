# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict = {}
        for i in range(n):
            # First check that target-nums[i] exists in dict or not
            if (target-nums[i]) in dict:
                # If element is exists return that element
                return [dict[target-nums[i]], i]
            # Adding current element in dict
            dict[nums[i]] = i