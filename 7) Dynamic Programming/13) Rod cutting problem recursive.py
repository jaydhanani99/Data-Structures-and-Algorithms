# https://www.youtube.com/watch?v=SZqAQLjDsag&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=14
# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

# We can cut the rod having same lengths, so this is the problem related to the unbounded knapsack
class Solution:
    def solve(self, weight, value, W, n):
        if n == 0 or W == 0:
            return 0

        if weight[n-1] <= W:
            return max((value[n-1]+self.solve(weight, value, W-weight[n-1], n), self.solve(weight, value, W, n-1)))
        return self.solve(weight, value, W, n-1)
    def rodcutting(self, price):
        # This is the same problem as unbounded knapsack
        # We have price array instead of value array
        # We have len(price) as N instead of W
        # We have weight array as [1,2,....,N]

        value = price
        W = len(price)
        weight = [i for i in range(1, W+1)]
        n = len(price)

        return self.solve(weight, value, W, n)





sol = Solution()

# Price to cut the rod of length (i+1), e.g price to cut the second rod is 5
price = [1, 5, 8, 9, 10, 17, 17, 20]

print(sol.rodcutting(price))