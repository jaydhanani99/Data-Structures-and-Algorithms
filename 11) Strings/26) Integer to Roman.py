# https://leetcode.com/problems/integer-to-roman/
# https://www.interviewbit.com/old/problems/integer-to-roman/
# https://practice.geeksforgeeks.org/problems/convert-to-roman-no/1


class Solution:
    def intToRoman(self, number: int) -> str:
        # Refer: https://projecteuler.net/about=roman_numerals
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        return "M"*(number//1000)+hundreds[(number%1000)//100]+tens[(number%100)//10]+ones[(number%10)]
        
        
        # Another approach
        ans     =       ""
        while(number > 0):
            if number >= 1000:
                ans     +=  "M"
                number       -=  1000
            elif number >= 500:
                if number >= 900:
                    ans +=  "CM"
                    number   -=  900
                else:
                    ans +=  "D"
                    number   -=  500
            elif number >= 100:
                if number >= 400:
                    ans +=  "CD"
                    number   -=  400
                else:
                    ans +=  "C"
                    number   -=  100
            elif number >= 50:
                if number >= 90:
                    ans +=  "XC"
                    number   -=  90
                else:
                    ans +=  "L"
                    number   -=  50
            elif number >= 10:
                if number >= 40:
                    ans +=  "XL"
                    number   -=  40
                else:
                    ans +=  "X"
                    number   -=  10
            elif number >= 5:
                if number >= 9:
                    ans +=  "IX"
                    number   -=  9
                else:
                    ans +=  "V"
                    number   -=  5
            else:
                if number >= 4:
                    ans +=  "IV"
                    number   -=  4
                else:
                    ans +=  "I"
                    number   -=  1
        return ans
                    
            