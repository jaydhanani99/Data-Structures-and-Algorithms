# https://www.youtube.com/watch?v=_gPcYovP7wc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=7
# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
# https://www.interviewbit.com/problems/subset-sum-problem/

class Solution:
    def solve(self, input_array, sum):
        # Consider input_array as item array same as knapsack
        # Similarly we have given sum instead of W (total weight)
        # So we create matrix of n*sum and instead of storing maximum sum in matrix we store True/False which denotes sum is possible or not at this point
        n = len(input_array)
        matrix = [[None for i in range(sum+1)] for j in range(n+1)]
        
        # Now for example we are at point i, j in matrix
        # So this point denotes whether it is possible to sum j with either including subset arr[i] or without including
        # For the first row we have i = 0 which means we do not have any number for sum
        # So for the i = 0 we have empty subset and with the empty subset we can have sum = 0
            # So for i = 0 and j = 0 our matrix value would be True
        # now for i = 0 and j = 1 that means we cannot have sum = 1 with empty subset
        # so matrix value for i = 0 and j > 0 would be False
        # In the same manner for i > 0 we can have sum = 0 by not including any subset
        # so matrix value for i > 0 and j = 0 would be True

        for i in range(n+1):
            matrix[i][0] = True
        for j in range(1, sum+1):
            matrix[0][j] = False

        # Now we traverse the matrix
        for i in range(1, n+1):
            for j in range(1, sum+1):
                # i-1 is the current element of input_array
                # so if current_element is less than or equal to the sum we required which is j
                if input_array[i-1] <= j:
                    # if so we have two cases
                    # 1) If we include element then we need to check that (required sum - element) was possible before or not if it was possible that means this also be possible
                    # 2) If we do not include element then our sum is possible only if it was possible before
                    matrix[i][j] = matrix[i-1][j-input_array[i-1]] or matrix[i-1][j]
                else:
                    # If input_array[i-1] > j that means we cannot include current element
                    # so our sum j is possible only if it was possible before
                    matrix[i][j] = matrix[i-1][j]
        
        return matrix[n][sum]

sol = Solution()
input_array = [2, 3, 7]

sum = 5

print(sol.solve(input_array, sum))