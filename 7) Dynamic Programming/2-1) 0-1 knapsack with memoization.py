# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.youtube.com/watch?v=fJbIuhs24zQ&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=4
# https://www.interviewbit.com/problems/0-1-knapsack/

class Solution:
    def solve(self, weight, value, W, n, matrix):
        # Base condition
            # 1) n == 0 means we do not have item left to put in bag
            # 2) W == 0 means we have filled all the space of bag
        if n == 0 or W == 0:
            return 0

        # if we have already done this recursive call then return directly from here
        if matrix[n][W]:
            return matrix[n][W]

        # if last item weight is less then the remaining size of bag
        if weight[n-1] <= W:
            # Then we have two options either include current item or not include
            # Including the last item (update the remaining bag size and n as n-1 for last item in next iteration)
            # Or not including the current item 
            #       (as we have not included the item we do not update the remaining bag size, and n as n-1 for last item in next iteration)

            # We return maximum of both the possibility
            # Memoizing current recursive function call value in matrix
            matrix[n][W] = max((value[n-1]+self.solve(weight, value, W-weight[n-1], n-1, matrix)), 
                            (self.solve(weight, value, W, n-1, matrix)))
            return matrix[n][W]
        
        # If current item weight is greater than the remaining bag size we do not include the current item
        # Memoizing current recursive function call value in matrix
        matrix[n][W] = self.solve(weight, value, W, n-1, matrix)
        return matrix[n][W]


    # should return maximum profit
    def knapsack(self, weight, value, W):
        # For the memoization we first look at the values that are being changed at every recursion step
        # So here we have W and n which is changing at every recursion step
        # So to memoize the recursion we create matrix of size n*W
        # After finding the profit for the W and n-1 we store it in matrix
        # So if we encounter the same arguements we can directly use it
        # Here we are solving the problem by recursively finding the solution to the smaller sub problems which is the top-down approach.
        # Top-down approach: Start with Bigger problem and recursively solve smaller problem as needed
        n = len(weight)
        matrix = [[None for i in range(W+1)] for j in range(n+1)]
        return self.solve(weight, value, W, n, matrix)









sol = Solution()
# Weight of item
weight = [1, 2, 3]

# Profit of item
value = [60, 100, 120]

# capacity of bag
W = 5
print(sol.knapsack(weight, value, W))