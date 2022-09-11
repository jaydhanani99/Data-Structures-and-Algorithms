# https://www.youtube.com/watch?v=I4UR2T6Ro3w&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=16
# https://www.geeksforgeeks.org/coin-change-dp-7/
# https://leetcode.com/problems/coin-change-2/


class Solution:
    def maximumWays(self, coin, sum):
        n = len(coin)
        matrix = [[None for i in range(sum+1)] for j in range(n+1)]

        # for sum = 0 we have only one pair which is empty set
        for i in range(n+1):
            matrix[i][0] = 1
        
        for j in range(1, sum+1):
            matrix[0][j] = 0

        for i in range(1, n+1):
            for j in range(1, sum+1):
                if coin[i-1] <= j:
                    # instead of matrix[i-1][j-coin[i-1]] we would write matrix[i][j-coin[i-1]] for unbounded knapsack
                    matrix[i][j] = matrix[i][j-coin[i-1]] + matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j]

        return matrix[n][sum]


sol = Solution()
coin = [1,2,3]
N = 4

print(sol.maximumWays(coin, N))