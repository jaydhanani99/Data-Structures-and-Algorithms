# Remove (size//2 + 1)th element from stack

# https://www.youtube.com/watch?v=AZ4jEY_JAVc&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=6

class Solution:
    # We need to delete kth element
    def remove(self, nums, k):
        if k == 1:
            nums.pop()
            return
        k -= 1
        element = nums.pop()
        self.remove(nums, k)
        nums.append(element)
    
    def removeMiddleElement(self, nums):
        n = len(nums)
        if n == 0:
            return []
        k = n//2 + 1
        self.remove(nums, k)
        return nums

sol = Solution()
print(sol.removeMiddleElement([4, 5, 6]))