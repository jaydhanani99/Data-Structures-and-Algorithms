# https://www.youtube.com/watch?v=SZqAQLjDsag&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=14
# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

# We can cut the rod having same lengths, so this is the problem related to the unbounded knapsack
class Solution:
    def solve(self, weight, value, W, n):

        matrix = [[None for i in range(W+1)] for j in range(n+1)]

        for i in range(n+1):
            matrix[i][0] = 0
        for j in range(W+1):
            matrix[0][j] = 0

        for i in range(1, n+1):
            for j in range(1, W+1):
                if weight[i-1] <= j:
                    # For the unbounded knapsack there is only one change here,
                    # Instead of using matrix[i-1][j-weight[i-1] we use matrix[i][j-weight[i-1]
                    # So actually in for loop we are adding value[i-1] which is the current item multiple times
                        # How ??
                        # => we update the matrix[i][j] and after adding current item we look for answer
                        # that what is the maximum value for remaining weight which is j-weight[i-1]
                        # If we look in previous row that means we check maximum answer when we have item only once
                        # However if we look into current row that means we are adding item in current row increamentally,
                        # that's why we have kept i instead of i-1
                        # So in short for bounded knapsack we are adding answer in matrix[i][j] based on the previous row only
                        # However for unbounded we are adding answer based on current row and previous row
                            # for the current row we include the item using value[i-1], because for current row,
                            #  at every column we store answer increamentally
                            # e.g value = [5, 7, 9] weight = [1, 2, 3] 
                            # W 0   1   2   3   4
                            # n
                            # 0 0   1   2   3   4    (i.e for W = 3 we have included 0th item weight which is 1 for 3 times)
                            # 1
                            # 2  
                    matrix[i][j] = max((value[i-1]+matrix[i][j-weight[i-1]]), matrix[i-1][j])
                else:
                    matrix[i][j] = matrix[i-1][j]
        return matrix[n][W]
        
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