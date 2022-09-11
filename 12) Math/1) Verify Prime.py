# https://www.interviewbit.com/old/problems/verify-prime/

class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, number):
	    n = int(number**(0.5)+1)
        for i in range(2, n):
            if number%i == 0:
                return 0
        return 1 if number != 1 else 0