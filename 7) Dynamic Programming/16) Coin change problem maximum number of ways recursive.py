# https://www.youtube.com/watch?v=I4UR2T6Ro3w&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=16
# https://www.geeksforgeeks.org/coin-change-dp-7/
# https://leetcode.com/problems/coin-change-2/


class Solution:
    def solve(self, coin, sum, n):

        # for sum 0 we have only 1 option which empty subset (obviously 0 is not allowed in case of coin)
        if sum == 0:
            return 1
        
        # for n == 0 means we do not have any coins so possibility is zero if sum is not zero
        if n == 0:
            return 0

        if coin[n-1] <= sum:
            # Now we have two options either we include coin or not
            # We would use same coin if possible that's why n instead of n-1 (in case of including current coin)
            return self.solve(coin, sum-coin[n-1], n) + self.solve(coin, sum, n-1)
        else:
            return self.solve(coin, sum, n-1)
        


    def maximumWays(self, coin, N):
        # We have given coins and we need to form sum by using that coins
        # We can use same coin multiple times (This is the indication of unbounded knapsack)
        # Now we need to find the number of ways we can do the sum N (which is the same as count of subset sum)
        # So basically this problem is combination of count of subset sum and unbound knapsack

        n = len(coin)

        return self.solve(coin, N, n)

sol = Solution()
coin = [1,2,3]
N = 4

print(sol.maximumWays(coin, N))