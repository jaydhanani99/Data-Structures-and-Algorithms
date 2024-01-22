# https://www.interviewbit.com/old/problems/fizzbuzz/
# https://leetcode.com/problems/fizz-buzz/


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output   =   [str(i) for i in range(1, n+1)]
        
        for i in range(3, n+1, 3):
            output[i-1] = 'Fizz'
        for i in range(5, n+1, 5):
            output[i-1] = 'Buzz'
        for i in range(15, n+1, 15):
            output[i-1] = 'FizzBuzz'
        return output

        # Another approach
        output = []
        for i in range(1, n+1):
            if i%3  ==  0 and i%5 == 0:
                output.append('FizzBuzz')
            elif i%3  ==  0:
                output.append('Fizz')
            elif i%5 == 0:
                output.append('Buzz')
            else:
                output.append(str(i))
        return output