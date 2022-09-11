# Count the number of subset with a given difference


class Solution:
    def countSubsetSum(self, input_array, sum):
        n = len(input_array)
        
        matrix = [[None for i in range(sum+1)] for j in range(n+1)]

        for i in range(n+1):
            matrix[i][0] = 1
        for j in range(1, sum+1):
            matrix[0][j] = 0

        for i in range(1, n+1):
            for j in range(1, sum+1):
                if input_array[i-1] <= j:
                    matrix[i][j] = matrix[i-1][j-input_array[i-1]]+matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j]
        return matrix[n][sum]
        
    def solve(self, input_array, given_difference):
        # Here difference between two sum is given
        # So S1 - S2 = given_difference
        # and we have S1 + S2 = total_sum
        # so S1 would be (given_difference+total_sum)//2
        # So we need to count subset for which sum is (given_difference+total_sum)//2
        total_sum = sum(input_array)
        return self.countSubsetSum(input_array, (given_difference+total_sum)//2)



sol = Solution()
input_array = [1,1,1,1,1]
given_difference = 3
print(sol.solve(input_array, given_difference))