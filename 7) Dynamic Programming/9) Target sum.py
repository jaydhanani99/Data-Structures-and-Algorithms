# https://leetcode.com/problems/target-sum/submissions/

class Solution:
    def countSubsetSumRecursiveMemoize(self, input_array, sum, n, matrix):
        # we can have count = 1 for {} empty set only as we are considering 0 in input_array
        if sum == 0 and n == 0:
            return 1
        
        if n == 0:
            return 0
        
        # Check Memoized answer
        if matrix[n][sum] is not None:
            return matrix[n][sum]
        
        if input_array[n-1] <= sum:
            matrix[n][sum] = self.countSubsetSumRecursiveMemoize(input_array, sum-input_array[n-1], n-1, matrix) + self.countSubsetSumRecursiveMemoize(input_array, sum, n-1, matrix)
            return matrix[n][sum]
        matrix[n][sum] = self.countSubsetSumRecursiveMemoize(input_array, sum, n-1, matrix)
        return matrix[n][sum]
    
    
    def countSubsetSum(self, input_array, sum):
        n = len(input_array)
        
        matrix = [[None for i in range(sum+1)] for j in range(n+1)]

        # for i in range(n+1):
        # if n = 0 that means no element presents and required sum = 0 at that moment we have only 1 subset which is {}
        # Here we are not going to do count = 1 for all the n because we can have 0 in input element
        # So instead of staarting j loop from 1 to sum+1 we start it from 0 to sum+1 as we can have 0 in input elements too
        matrix[0][0] = 1
        
        for j in range(1, sum+1):
            matrix[0][j] = 0
            

        for i in range(1, n+1):
            # Instead of starting this loop from 1 to sum we start it from 0
            for j in range(0, sum+1):
                if input_array[i-1] <= j:
                    matrix[i][j] = matrix[i-1][j-input_array[i-1]]+matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j]
        return matrix[n][sum]
    
    def findTargetSumWays(self, input_array, target):
        # Here target sum is the difference of two sum as we are apply positive sign to some elements and negative sign to some elements
        # So let's say sum of positive signed elements is S1 and sum of negative signed elements is S2
        # we have S1-S2 = target
        # and we also have S1+S2 = total_sum
        # So this is the same problem as the Count number of subset with given difference
        # From both the equation 2S1 = total_sum + target => S1 = (total_sum+target)/2
        
        # However there is one change here
        # For the subset sum difference we are not including 0 as input element, so we are assuming count 1 for sum = 0
        # That means if sum = 0 that means we have only 1 subset and which is {} empty subset
        # However if we inlclude 0 in input element we can have subset {0} which sum is also 0
        # so for example if we have input_array = [0, 0, 0] and target sum is 0 we can have following subset for which some is 0
            # 1) {}
            # 2) {0 (1st position)}
            # 3) {0 (2nd position)}
            # 4) {0 (3rd position)}
            # 5) {0(1st position), 0(2nd position)}
            # 6) {0(2nd position), 0(3rd position)}
            # 7) {0(1st position), 0(3rd position)}
            # 8) {0, 0, 0}
        # so if we assume count as 1 for (sum = 0, and n from 0 to n) we will get wrong answer in this problem
        total_sum = sum(input_array)
        
        # That means S1 and S2 group is not possible
        if (total_sum + target)%2 != 0:
            return 0
        
        # So we need count subset sum for (total_sum+target)//2
        return self.countSubsetSum(input_array, (total_sum+target)//2)
        
        
        # Recursive Memoize solution
        # matrix = [[None for i in range(((total_sum+target)//2)+1)] for j in range(len(input_array)+1)]
        # return self.countSubsetSumRecursiveMemoize(input_array, (total_sum+target)//2, len(input_array), matrix)