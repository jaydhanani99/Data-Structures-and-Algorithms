# https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/
# https://www.youtube.com/watch?v=8YXQ68oHjAs&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=9

class Solution:
    # This will be used to insert element at last position
    def insert(self, nums, element):
        if len(nums) == 0:
            nums.append(element)
            return
        last_element = nums.pop()
        self.insert(nums, element)
        nums.append(last_element)

    def reverse(self, nums):
        if len(nums) == 0:
            return
        element = nums.pop()
        self.reverse(nums)
        self.insert(nums, element)
        return nums


sol = Solution()
print(sol.reverse([4, 5, 6]))