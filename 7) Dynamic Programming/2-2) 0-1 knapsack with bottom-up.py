# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.youtube.com/watch?v=ntCGbPMeqgg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=5
# https://www.interviewbit.com/problems/0-1-knapsack/

class Solution:
    # should return maximum profit
    def knapsack(self, weight, value, W):
        n = len(weight)
        matrix = [[None for i in range(W+1)] for j in range(n+1)]

        # top-down approach is same as the memoization matrix
        # Instead of doing recursive call we iterate through matrix and get answer at index [n][W]
        # first row and column of matrix is the initialization which is the base condition in terms of recursive solution
        # We have written base condition as if n == 0 or W == 0: return 0 that means for n == 0 or W == 0 our answer is 0
        # Same thing we will do in matrix for the row n == 0 and for the column W == 0 we initialize values with 0
        # So first row and first column should be filled with zero
        for i in range(n+1):
            matrix[i][0] = 0
        for j in range(W+1):
            matrix[0][j] = 0

        # If you look solution of memoization we start from n and W and going towards 0 and 0
        # Which is the top-down approach in tree like structure
        # In this approach we are actually going from bottom-up approach if you compare it with tree like sturecture
        # Because in iterative solution we start from 0 and 0 and going towards n and W
        # Bottom Up Approach: Start by solving all related subproblems until you build result to the main problem.

        # Traverse in items and based on the remaining weight we decide whether to include item or not
        for i in range(1, n+1):
            # Traverse through remaining weights (we assume we have bag size is j)
            for j in range(1, W+1):
                # if weight[i-1] <= j that means we can include current item as we have enough remaining space j in bag
                if weight[i-1] <= j:
                    # So we have two options either include current item in this bag or not
                    # 1) If we include current item which is i-1 as per the index, in this bag
                        # we add value[i-1] profit to our answer, which is the profit for the current item
                        # Also we add previous answer which lies in row matrix[i-1]
                        # Now we have included current item which weight is weight[i-1] so remaining weight for current bag would be j-weight[i-1]
                        # So we look for j-weight[i-1] in previous row which is matrix[i-1][j-weight[i-1]]
                        
                    # 2) If we do not include current item in this bag then
                        # we include previous answer with weight same as current remaining weight which is j as we have not included any item
                    matrix[i][j] = max((value[i-1]+matrix[i-1][j-weight[i-1]]), matrix[i-1][j])

                # That means we do not have remaining space to include current item so for this case our answer would be the
                #     previous answer for the same remaining bag size which is j
                else:
                    matrix[i][j] = matrix[i-1][j]


        # Example matrix for weight = [1, 2, 3], value = [60, 100, 120], W = 5
        # so we have n = 3 and W = 5 
                        # Remaining weight => W
        #         0       1       2       3       4       5
        # n
        # 0       0       0       0       0       0       0

        # 1       0     60+0    60+0    60+0    60+0    60+0

        # 2       0     max(60, max(60, max(60, max(60, max(60,
        #               60+0)   100+0)  100+60) 100+60) 100+60)

        # 3       0     60      100     max(160, max(160, max(160,
        #                               120+0)   120+60)  120+100)


        return matrix[n][W]









sol = Solution()
# Weight of item
weight = [1, 2, 3]

# Profit of item
value = [60, 100, 120]

# capacity of bag
W = 5
print(sol.knapsack(weight, value, W))