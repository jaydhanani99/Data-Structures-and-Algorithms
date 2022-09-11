# https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # First approach is to use cycle detection, this would calculate in O(n) time and O(1) space
        # This would also work for particular elment is occure multiple times
        # Refer solution approach 3: Floyd's Tortoise and Hare (Cycle Detection) of https://leetcode.com/problems/find-the-duplicate-number
        # The idea is to first find the cycle in the nums
        # we take two pointer one is slow and second is fast
        # Initially both pointer points to the value of first element
        # now we move slow to nums[slow] and fast to nums[nums[fast]]
        # At some point both pointer would point to the same element because list have duplicate elements
        # Note that the intersection point is not the cycle entrance in the general case.
        

        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Now our task is to find the repetitive element
        # Now we point slow to the starting position
        # and we traverse slow and fast by one position only
        # When both points at the same position we would get our repetitive elements
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
        
        # Second approach (This would work only if particular element is occure two times) in O(n) time and O(1) space
        # n = len(nums)
        # total_sum = sum(nums)
        # actual_sum = n*(n+1)//2
        # diff = actual_sum - total_sum
        # return n - diff
    
    
        # Another solution would be using map with extra space
        # dict = {}
        # for x in nums:
        #     if x in dict:
        #         return x
        #     else:
        #         dict[x] = 1