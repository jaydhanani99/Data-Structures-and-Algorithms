# https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=10
# https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1
# https://www.interviewbit.com/problems/minimum-difference-subsets/

class Solution:
    def subsetsum(self, input_array, sum):
        n = len(input_array)
        matrix = [[None for i in range(sum+1)] for j in range(n+1)]

        for i in range(n+1):
            matrix[i][0] = True
        for j in range(1, sum+1):
            matrix[0][j] = False

        for i in range(1, n+1):
            for j in range(1, sum+1):
                if input_array[i-1] <= j:
                    matrix[i][j] = matrix[i-1][j-input_array[i-1]] or matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j]
        return matrix
        
    def solve(self, input_array):
        # Now we need to divide input_array into two subset in such a way that difference between sum of two subset will be minimum
        # Now let's say we have two subset S1 and S2 and their minimum difference of sum is x
        # so S1-S2 = x
        # Now when minimum difference is zero at that moment sum of two subset would be the same i.e S1 = S2
        # In the worst case we have one subset without any elements and another subset with all the array values
        # So at that momen S1 = 0 and S2 = sum(array)
        # So difference between two subsets will be in between 0 and sum(array)
        # So we have S1+S2 = total_sum
        # now if we increase S1, S2 will be decreased
        # If we consider difference as 0 at that moment S1 and S2 would be the same, i.e 2S1 = total_sum => S1 = total_sum//2
        # So we try to find the S1 and S2 would automatically be total_sum - S1
        # and now we have range between 0 and total_sum//2 instead of 0 and total_sum as S1 and S2 would be inversely proportional 
        # so it does not matter we find S1 or S2
        total_sum = sum(input_array)
        # Initially we take our answer as total_sum
        answer = total_sum
        # Creating matrix for whole sum using subsetsum,
        #  and based on that we identify that sum (i) is possible or not which is the subproblem of total_sum
        # Infact we are checking for the total_sum//2 so we find subsetsum possibility for total_sum//2 only
        matrix = self.subsetsum(input_array, total_sum//2)
        n = len(input_array)

        # Now we start loop from maximum possible S1 so that when we encounter first S1 which is the maximum S1
            # We can have S2 as (total_sum-max(S1)) so at that this point difference between S1 and S2 would be minimum
        for i in range((total_sum//2), -1, -1):
            is_subset_sum_possible = matrix[n][i]
            if is_subset_sum_possible == True:
                S1 = i
                S2 = (total_sum-i)
                answer = min(abs(S1-S2), answer)
                # Directly returning answer if we encounter maximum S1
                return answer
        return answer

sol = Solution()
input_array = [1, 6, 11, 5]

print(sol.solve(input_array))