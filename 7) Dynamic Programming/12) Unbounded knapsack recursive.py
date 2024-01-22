# https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/

class Solution:
    def solve(self, weight, value, W, n):

        # same as bounded knapsack
        if n == 0 or W == 0:
            return 0

        if weight[n-1] <= W:
            # Now we include current item however we will not going to take next item instead we take current item in next iteration
            # To do so instead of decreamenting n we keep it n
            # Or we have another option not to include current item in that case we decreament n as we will look forward for the next item
            return max(value[n-1]+self.solve(weight, value, W-weight[n-1], n), self.solve(weight, value, W, n-1))
        else:
            # we will not include current item as it is not possible to take current item so we directly move to the next item
            return self.solve(weight, value, W, n-1)


    def knapsack(self, weight, value, W):
        n = len(weight)

        return self.solve(weight, value, W, n)




sol = Solution()
# Weight of item
weight = [1, 3, 4, 5]

# Profit of item
value = [10, 40, 50, 70]

# capacity of bag
W = 8
print(sol.knapsack(weight, value, W))