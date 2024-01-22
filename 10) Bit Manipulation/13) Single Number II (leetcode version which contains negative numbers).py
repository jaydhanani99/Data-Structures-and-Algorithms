# https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, numbers: List[int]) -> int:
        bln_negative = False
        result  =   0
        # the idea is that we will find the sum of set bits (bit that contain 1) of all numbers at every position
        # so we start from first position and we find the sum
        # at last we modulo it with 3 if it is zero that means this bit of number which occures once is zero
        # if mod is not zero that means this bit of number which occures once is one
        # we store this bit in result using or operation
        # at last we finally get the number that is not repeated three times in result
        # Iterate for every bit position
        for i in range(0, 32):
            sum         =   0
            # Used to check if ith bit is 1 or not.
            currentBit  =   (1 << i) #it will be look like 0001, 0010, 0100, 1000 and so on for each loop
            for j in range(0, len(numbers)):
                # finding sum of set bit at ith position
                # This will only be true, if ith bit is set (=1)
                if (numbers[j] & currentBit) > 0:
                    sum     +=  1
                
            # Set ith bit  of result based on whether the ith bit occured 3 times or not.
            # Only the bits that occured 1 time will be 1
            if (sum % 3)    !=  0:
                result  =   result  |   currentBit
                
        # For the last iteration if sum % 3 != 0 that means non repeating number is negative as MSB represents the signed bit (0 => Positive, 1 => Negative)
        if sum % 3 != 0:
            # negative number is represented by 2's complement
            # e.g. 4 (000....100) then -4 will be represented as (111...100)
            # 2's complement is calculated by (toggle all the bits + 1)
            # Now for example our result is -4 then python would interprit as unsigned number
            # so to convert it to negative number we do -(2's complement of number) => by finding 2's complement we are finding the actual number and we negate them manually
            
            # Finding 2's complement of result
            for j in range(32):
                result = result^(1<<j)
            result += 1
            # Negate the number
            result = -result
        return result