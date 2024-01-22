# https://www.interviewbit.com/old/problems/roman-to-integer/
# https://leetcode.com/problems/roman-to-integer
# https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, string):
        dict1 = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        dict2 = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        i = 0
        n = len(string)
        ans = 0
        while i+1 < n:
            if string[i]+string[i+1] in dict1:
                ans += dict1[string[i]+string[i+1]]
                i += 2
            else:
                ans += dict2[string[i]]
                i += 1
        if i != n:
            ans += dict2[string[i]]
        return ans
        
        # Another approach
        A = string
        ans     =       0
        i       =       len(A)-1
        while(i >= 0):
            if A[i] == 'I':
                ans     +=  1
                i       -=  1
            elif i > 0 and A[i] == 'V' and A[i-1] == 'I':
                ans     +=  4
                i       -=  2
            elif A[i] == 'V':
                ans     +=  5
                i       -=  1
            elif i > 0 and A[i] == 'X' and A[i-1] == 'I':
                ans     +=  9
                i       -=  2
            elif A[i] == 'X':
                ans     +=  10
                i       -=  1
            elif i > 0 and A[i] == 'L' and A[i-1] == 'X':
                ans     +=  40
                i       -=  2
            elif A[i] == 'L':
                ans     +=  50
                i       -=  1
            elif i > 0 and A[i] == 'C' and A[i-1] == 'X':
                ans     +=  90
                i       -=  2
            elif A[i] == 'C':
                ans     +=  100
                i       -=  1
            elif i > 0 and A[i] == 'D' and A[i-1] == 'C':
                ans     +=  400
                i       -=  2
            elif A[i] == 'D':
                ans     +=  500
                i       -=  1
            elif i > 0 and A[i] == 'M' and A[i-1] == 'C':
                ans     +=  900
                i       -=  2
            else:
                ans     +=  1000
                i       -=  1
        return ans