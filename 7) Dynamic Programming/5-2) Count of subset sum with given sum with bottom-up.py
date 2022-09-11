# https://www.youtube.com/watch?v=F7wqWbqYn9g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=9
# https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/


class Solution:
    def countSubsetSumBottomUp(self, input_array, input_sum):
        # Now we do same as the subset sum
        # Difference is that in subset sum we are storing True and False, 
        #   however in this instead of True/False we store count of the pair for every sum column

        # So we have matrix of size n*input_sum
        n = len(input_array)
        matrix = [[None for i in range(input_sum+1)] for j in range(n+1)]

        # Now for first column we can have sum with 0 for any subset so we set first column as 1
        for i in range(n+1):
            matrix[i][0] = 1
        
        # For first row from the 2nd column we do not have any subset so we cannot do sum which is from 1 to input_sum+1 for each column
        for j in range(1, input_sum+1):
            matrix[0][j] = 0


        for i in range(1, n+1):
            for j in range(1, input_sum+1):
                # That means sum is possible
                if input_array[i-1] <= j:
                    # Now we have two options either include current element in subset or not
                    # 1) If we include element then we need to add (required sum - element) possible subset in previous sum
                    # 2) If we do not include element then we need to add subset count as it was before
                    matrix[i][j] = matrix[i-1][j-input_array[i-1]] + matrix[i-1][j]
                else:
                    # Else we do not include element and we add subset count as it was before
                    matrix[i][j] = matrix[i-1][j]
        return matrix[n][input_sum]

    def countSubsetSum(self, input_array, input_sum):
        # # count subsetsum using bottom-up approach
        return self.countSubsetSumBottomUp(input_array, input_sum)

sol = Solution()
input_array = [0, 0, 0, 0, 0, 0, 0, 1]
input_sum = 1

print(sol.countSubsetSum(input_array, input_sum))