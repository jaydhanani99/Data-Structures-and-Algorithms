# https://www.youtube.com/watch?v=_gPcYovP7wc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=7
# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
# https://www.interviewbit.com/problems/subset-sum-problem/

class Solution:
    def solve(self, input_array, remaining_sum, n):
        # if remaining_sum == 0 that means if we have item or not we can have sum = 0
        if remaining_sum == 0:
            return True
        # if n == 0 that means we do not have any item to sum so only 0 sum is possible which we have returned before
        if n == 0:
            return False


        # if input_array[n-1] which is the last remaining item in input_array is less than the remaining_sum that means we can include this item in sum
        if input_array[n-1] <= remaining_sum:
            # We have two options
            # 1) We include input_array[n-1] in remaining_sum
            # 2) Or we do not include item in remaining_sum
            return self.solve(input_array, remaining_sum-input_array[n-1], n-1) or self.solve(input_array, remaining_sum, n-1)
        
        # Else we cannot include current item in remaining_sum
        return self.solve(input_array, remaining_sum, n-1)

    def subsetsum(self, input_array, sum):
        return self.solve(input_array, sum, len(input_array))

sol = Solution()
input_array = [2, 3, 7]

sum = 5

print(sol.subsetsum(input_array, sum))