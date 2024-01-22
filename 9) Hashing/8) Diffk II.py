# https://www.interviewbit.com/problems/diffk-ii/

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, numbers, k):
        dict = {}
        # Here we have asked for difference k
        # The difference is defined as numbers[i] - numbers[j] if numbers[i] > numbers[j]
        #                           or numbers[j] - numbers[i] if numbers[j] > numbers[i]
        # So we have two options to check for k = numbers[i] - numbers[j]
        # k + numbers[i] (which is actually numbers[j]) or numbers[i] - k
        n = len(numbers)
        for i in range(n):
            if k+numbers[i] in dict or numbers[i]-k in dict:
                return 1
            dict[numbers[i]] = i
        return 0