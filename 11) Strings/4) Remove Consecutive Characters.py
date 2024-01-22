# https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1

class Solution:
    def removeConsecutiveCharacter(self, string):
        n = len(string)
        i = 0
        output = []
        
        while i < n:
            while i+1 < n and string[i] == string[i+1]:
                i += 1
            output.append(string[i])
            i += 1
        return ''.join(output)