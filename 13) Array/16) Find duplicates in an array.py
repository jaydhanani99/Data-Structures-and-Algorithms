# https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	dict = {}
    	output = []
    	for x in arr:
    	    if x not in dict:
	            dict[x] = 1
	        else:
	           dict[x] += 1
	    for key in dict:
	        if dict[key] > 1:
                output.append(key)
        return sorted(output) if output else [-1]