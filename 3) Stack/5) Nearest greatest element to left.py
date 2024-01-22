# Same question as 4) Nearest smaller element to left
# https://www.youtube.com/watch?v=T5s96ynzArg&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=3


class Solution:
    def solve(self, input_array):
        stack = []
        answer = []

        for x in input_array:
            while stack and stack[-1] <= x:
                stack.pop()
            if stack:
                answer.append(stack[-1])
            else:
                answer.append(-1)

            stack.append(x)
        return answer 

input_array = [10, 5, 11, 10, 20, 12]
s1 = Solution()
print(s1.solve(input_array))

