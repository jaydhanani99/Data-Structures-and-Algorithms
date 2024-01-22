# https://www.interviewbit.com/old/problems/prime-sum/

import math 
class Solution:
    def isPrime(self, num):
        for j in range(2, int(math.sqrt(num))+1):
            if num%j == 0:
                return False
        return True
    # @param A : integer
    # @return a list of integers
    def primesum(self, n):
        for i in range(2, n+1):
            if(self.isPrime(i) and self.isPrime(n-i)):
                return [i, n-i]
                
                
        
        # Another approach by finding the prime numbers using sieve of eratosthenes
        prime = [True for i in range(n+1)]
        p = 2
        
        while(p*p <= n):
            # prime[p] == True that means we need to check whether it is actual prime or not.
            if(prime[p] == True):
                # Now we start with p*p and increament with p and mark it as non prime number(False), because it is divisible by these numbers.
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p   +=  1
            
        for i in range(2, n+1):
            if prime[i] and prime[n-i]:
                return [i, n-i]