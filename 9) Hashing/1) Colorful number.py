# https://www.interviewbit.com/old/problems/colorful-number/

class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, number):
        # To track the product of number
        dict = {}
        
        number = str(number)
        for i in range(len(number)):
            current_number = int(number[i])
            # Checking for individual number
            if current_number in dict:
                return 0
            
            # Adding current number in dict
            dict[current_number] = 1
                
            for j in range(i+1, len(number)):
                current_number *= int(number[j])
                # Checking for current product
                if current_number in dict:
                    return 0
                # Adding current product in dict
                dict[current_number] = 1
        return 1