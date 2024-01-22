# https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1
# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, numbers: List[int]) -> List[int]:
        # If we can break the array in two halves such that one non-repeating number would be in first half and second non-repeating number would be in second half we can easily get the answer by xor of all the elements in first and second half as xor of same element would be zero
        
        # Now we also want to make sure that same element would be in the same half
        
        # The idea is we first find the xor of the the elements in the array
        # Now we find the first LSB which has 1 (set bit) say it as kth bit, that means first and second elements have different bits at this position
        # Now we traverse through array and add the elements which has kth bit set in the first half and other in second half
        # by doing so we have elements which kth bit is set in first half and also first number which is non repeating
        # and kth bit is not set in second half and also second number which is non repeating
        # after that we do xor of all the elements in both the halves and we would get our answer
        
        # Taking initially xor as 0 because xor of any number with 0 would be 0
        xor = 0
        n = len(numbers)
        for i in range(n):
            xor ^= numbers[i]
        
        for k in range(32):
            if (xor & 1 << k) > 0:
                break
        # now we have kth set bit in k variable
        
        first_num = 0
        second_num = 0
        for i in range(n):
            if (numbers[i] & 1 << k) > 0:
                first_num ^= numbers[i]
            else:
                second_num ^= numbers[i]
        return [first_num, second_num]
                
                