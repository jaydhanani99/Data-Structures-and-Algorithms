# https://www.interviewbit.com/problems/largest-rectangle-in-histogram/
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# https://www.youtube.com/watch?v=J2X70jj_I1o&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=7
class Solution:
    def solve(self, input_array):
        n = len(input_array)
        answer = 0
        stack = []
        left = []
        right = []

        # For each element we just need to find nearest smaller index to right and nearest smaller index to left
        # by doing that we can easily identify how many pillars are greater than or equal to the current pillars
        #    we simply multiply pillars count with current pillar height
        # So once we have nearest smaller element to left and right  with their indexes as array element
        # we can do right - left - 1 to find the total pillars count
        
        # First we will find left smaller index
        # If we don't have left smaller element we store -1 and in the same manner,
            # while finding right smaller element if we don't have right smaller element we store n (which is the last index + 1)
        # So actually we have lowest index -1 for left and highest index + 1 for right to balance

        # Finding left smaller indexes
        for i in range(n):
            while stack and stack[-1][1] >= input_array[i]:
                stack.pop()
            if stack:
                left.append(stack[-1][0])
            else:
                left.append(-1)
            stack.append((i, input_array[i]))

        # Finding right smaller indexes
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1][1] >= input_array[i]:
                stack.pop()
            if stack:
                right.append(stack[-1][0])
            else:
                # Appending right most index + 1
                right.append(n)
            stack.append((i, input_array[i]))
        # Answer would be reverse of right
        right = right[::-1]

        for i in range(n):
            answer = max(answer, (right[i]-left[i]-1)*input_array[i])
        return answer


    # -----------------------------------------------------Another approach----------------------------------------------------------------
    # def leftSmallerPillars(self, input_array):
    #     left = []
    #     stack = []
    #     n = len(input_array)
    #     # Finding nearest smaller to left and store that pillar index in left array
    #     # storing nearest smaller element index and value in stack (index, value)
    #     for i in range(n):
    #         while stack and stack[-1][1] >= input_array[i]:
    #             stack.pop()
    #         if stack:
    #             left.append(i - stack[-1][0])
    #         else:
    #             left.append(i+1)
    #         stack.append((i, input_array[i]))
    #     return left
    # # @param A : list of integers
    # # @return an integer
    # def largestRectangleArea(self, input_array):
    #     answer = 0
    #     left = []
    #     right = [] 
 
    #     # For each element we just need to find nearest smaller index to right and nearest smaller index to left
    #     # by doing that we can easily identify how many pillars are greater than or equal to the current pillars
    #     #    we simply multiply pillars count with current pillar height
        
    
    #     left = self.leftSmallerPillars(input_array)
    #     # To find right smaller pillars we can simply reverse array and find left smaller pillars and again reverse the output
    #     #   By doing that we get the right smaller pillars count
    #     right = self.leftSmallerPillars(input_array[::-1])[::-1]
        
    #     # Now we just need to sum the left pillars and right pillars to find the total area
    #     n = len(input_array)
    #     for i in range(n):
    #         # Here left[i]+right[i]-1, -1 is because we have include current pillars in both left and right
    #         answer = max(answer, (left[i]+right[i]-1)*input_array[i])
    #     return answer

        
    
input_array = [6, 2, 5, 4, 5, 1, 6]
s1 = Solution()
print(s1.solve(input_array))