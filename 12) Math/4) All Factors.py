# https://www.interviewbit.com/old/problems/all-factors/
# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
	# @param A : integer
	# @return a list of integers
	def allFactors(self, n):
        # we would find the factor by loop till the sqrt(n)
        sqrt_n = int(n**(0.5))
        factors = []
        
        for i in range(1, sqrt_n+1):
            if n%i == 0:
                # Adding first factor
                factors.append(i)
                # Adding second factor by dividing n with i only if both are not same
                if i != n//i:
                    factors.append(n//i)
        return sorted(factors)