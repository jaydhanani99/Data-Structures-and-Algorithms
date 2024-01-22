# https://www.interviewbit.com/old/problems/prime-numbers/
# https://leetcode.com/problems/count-primes/
# https://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1

# Reference: https://www.geeksforgeeks.org/sieve-of-eratosthenes/

class Solution:
	# @param A : integer
	# @return a list of integers
	def sieve(self, n):
        # Creating initial list with value as True.
        # Initially we consider all the number as prime number later on we check and make it False if it's not.
        prime = [True for i in range(n+1)]
    
        # Starting with p = 2
        p = 2
        while(p*p <= n):
            # prime[p] == True that means we need to check whether it is actual prime or not.
            if(prime[p] == True):
                # Now we start with p*p and increament with p and mark it as non prime number(False), because it is divisible by these numbers.
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p   +=  1
    
        # After loop completes we traverse and print those number which flag is True.
        primeList = []
        for i in range(2, n+1):
            if prime[i]:
                primeList.append(i)
        return primeList


