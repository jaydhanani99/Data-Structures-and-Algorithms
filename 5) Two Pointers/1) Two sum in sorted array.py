# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/


class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        i = 0
        j = n-1
        
        # Using two pointer approach
        while i < j:
            current_sum = numbers[i]+numbers[j]
            if current_sum == target:
                return [i+1, j+1]
            elif current_sum < target:
                i += 1
            else:
                j -= 1
        return None