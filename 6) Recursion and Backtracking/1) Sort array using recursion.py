# https://www.youtube.com/watch?v=AZ4jEY_JAVc&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=6

class Solution:
    def insert(self, nums, element):
        # Here we consider nums is already sorted array and we want to insert the element to it
        # So if it is empty or element is greater then the last element than we simply insert element at last
        if len(nums) == 0 or nums[-1] <= element:
            nums.append(element)
            return
    
        # So if element should be in between elements of nums
        # than we remove the last element, call the insert function recursively and after that insert the last element
        last_element = nums.pop()
        self.insert(nums, element)
        nums.append(last_element)
        return
    
    def sortArray(self, nums):
        if len(nums) == 1:
            return nums
        # get last element from array and call sort again recursively
        element = nums.pop()
        self.sortArray(nums)
        # After sorting the remaining array we insert the temp element at sorted position
        self.insert(nums, element)
        return nums

sol = Solution()
print(sol.sortArray([4, 6, 2, 1, 15]))