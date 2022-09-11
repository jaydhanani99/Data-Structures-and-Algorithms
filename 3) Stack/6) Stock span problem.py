# Similar to previous smaller elements problem
# We need to find consecutive smaller element in left end side
# https://www.youtube.com/watch?v=p9T-fE1g1pU&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=6
# https://www.geeksforgeeks.org/the-stock-span-problem/
# https://leetcode.com/problems/online-stock-span/submissions/
class Solution:
    def solve(self, input_array):
        stack = []
        answer = []

        # n = len(input_array)

        # Here if we identify the position of nearest largest element of left,
        #   we can get the number of smaller elements between them which is our answer
        # In stack instead of storing larger element we store index of them so that we can count between elements

        # for i in range(n):
        #     while stack and stack[-1][1] <= input_array[i]:
        #         stack.pop()
        #     if stack:
        #         answer.append(i-stack[-1][0])
        #     else:
        #         answer.append(i+1)

        #     stack.append((i, input_array[i]))
        # return answer


        # Another way to do is by storing the total minimum elements and current element in stack
        for x in input_array:
            # Default answer would be 1
            current_answer = 1
            while stack and stack[-1][1] <= x:
                # Now for current smaller element we sum previously smaller elements if top stack element is less than the current element
                current_answer += stack.pop()[0]
            
            # After that we have our answer in current_answer we store it for current element in stack
            stack.append((current_answer, x))
            # Also we add current_answer to answer
            answer.append(current_answer)
        return answer

input_array = [100, 80, 60, 70, 60, 75, 85]
s1 = Solution()
print(s1.solve(input_array))