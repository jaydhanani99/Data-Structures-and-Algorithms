# Similar question to next greater element to right
# https://www.geeksforgeeks.org/next-smaller-element/
# https://www.youtube.com/watch?v=nc1AYFyvOR4&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=5

class Solution:
    def solve(self, input_array):
        stack = []
        answer = []
        n = len(input_array)

        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= input_array[i]:
                stack.pop()
            
            if stack:
                answer.append(stack[-1])
            else:
                answer.append(-1)
            
            stack.append(input_array[i])

        return answer[::-1]

input_array = [1, 3, 2, 4]
s1 = Solution()
print(s1.solve(input_array))