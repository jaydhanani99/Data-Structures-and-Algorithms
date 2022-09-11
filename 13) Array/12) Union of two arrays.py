# https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        dict = {}
        count = 0
        for x in a:
            if x not in dict:
                dict[x] = 1
                count += 1
        for x in b:
            if x not in dict:
                dict[x] = 1
                count += 1
        return count