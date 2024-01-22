# https://practice.geeksforgeeks.org/problems/palindrome-string0817/1

class Solution:
	def isPlaindrome(self, S):
	    return int(S == S[::-1])