# https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1

class Solution:
    def findPosition(self, number):
        # We can directly return the answer by finding the log(number) base 2
        # code here 
        if number == 0:
            return -1
        # We loop in number and right shift the bits until number > 0
        # If we encountered the 1 we right shift and stop
        # We check if number is zero now that means only 1 set bit we return that position
        position = 1
        while number > 0:
            if number & 1 == 1:
                number >>= 1
                break
            position += 1
            number >>= 1
        return position if number == 0 else -1