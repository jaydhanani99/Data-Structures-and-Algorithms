# https://www.interviewbit.com/problems/nearest-smaller-element/
# https://www.youtube.com/watch?v=85LWui3FlVk&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=4

class Solution:
    def solve(self, input_array):
        # Same question as next greater element to left
        # All we need to do is instead of starting from end of the array we will do from starting of the array
        # At last instead of returning reversed answer array we just return normal array as we have not started
        #    from the end of the input array

        stack = []
        answer = []

        for x in input_array:
            while stack and stack[-1] >= x:
                stack.pop()
            if stack:
                answer.append(stack[-1])
            else:
                answer.append(-1)
            
            stack.append(x)
        return answer

input_array = [1, 3, 2, 4]
s1 = Solution()
print(s1.solve(input_array))
