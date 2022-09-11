# https://www.youtube.com/watch?v=F7wqWbqYn9g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=9
# https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/


class Solution:
    def countSubsetSumRecursiveMemoize(self, input_array, remaining_sum, n, matrix):
        # Now we do same as the subset sum
        # Difference is that in subset sum we are storing True and False, 
        #   however in this instead of True/False we store count of the pair for every sum column.

        # if remaining_sum == 0 that means if we have item or not we can have sum = 0
        if remaining_sum == 0:
            return 1
        # if n == 0 that means we do not have any item to sum so only 0 sum is possible which we have returned before
        if n == 0:
            return 0
        
        if matrix[n][remaining_sum] is not None:
            return matrix[n][remaining_sum]

        if input_array[n-1] <= remaining_sum:
            # We have two options
            # 1) We include input_array[n-1] in remaining_sum
            # 2) Or we do not include item in remaining_sum
            matrix[n][remaining_sum] = self.countSubsetSumRecursiveMemoize(input_array, remaining_sum-input_array[n-1], n-1, matrix) + self.countSubsetSumRecursiveMemoize(input_array, remaining_sum, n-1, matrix)
            return matrix[n][remaining_sum]
        
        # Else we cannot include current item in remaining_sum
        matrix[n][remaining_sum] = self.countSubsetSumRecursiveMemoize(input_array, remaining_sum, n-1, matrix)
        return matrix[n][remaining_sum]

    def countSubsetSum(self, input_array, input_sum):
        n = len(input_array)
        matrix = [[None for i in range(input_sum+1)] for j in range(n+1)]

        return self.countSubsetSumRecursiveMemoize(input_array, input_sum, n, matrix)

sol = Solution()
input_array = [2, 3, 5, 6, 8, 10]
input_sum = 10

print(sol.countSubsetSum(input_array, input_sum))