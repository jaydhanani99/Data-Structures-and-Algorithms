# https://www.youtube.com/watch?v=St0Jf_VmG_g&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=8
# https://leetcode.com/problems/maximal-rectangle/
# https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/

class Solution:
    def largestRectangleHistogram(self, input_array):
        n = len(input_array)
        stack = []
        answer = 0
        left = []
        right = []

        for i in range(n):
            while stack and stack[-1][1] >= input_array[i]:
                stack.pop()
            if stack:
                left.append(stack[-1][0])
            else:
                left.append(-1)
            stack.append((i, input_array[i]))
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1][1] >= input_array[i]:
                stack.pop()
            if stack:
                right.append(stack[-1][0])
            else:
                right.append(n)
            stack.append((i, input_array[i]))
        right = right[::-1]

        for i in range(n):
            answer = max(answer, (right[i]-left[i]-1)*input_array[i])
        return answer

    
    def solve(self, input_array):
        # If we consider all the 1's of binary matrix as height of the pillars this problem is same as
        # the largest rectangle in histogram
        # So for each row we consider it as histogram value of base row is zero then we consider whole pillar as zero
        # So array [[1,0,1,0,0],  will be converted to [1,0,1,0,0] => [2,0,2,1,1] => [3,1,3,2,2] => [4,0,0,3,0]
        # and we find largestRectangleHistogram in [4, 1, 3, 3, 2]
        #           [1,0,1,1,1],
        #           [1,1,1,1,1],
        #           [1,0,0,1,0]]    
        r = len(input_array)
        c = len(input_array[0])
        rectangle_array = [0]*c
        answer = 0
        for i in range(r):
            for j in range(c):
                if input_array[i][j] == 0:
                   rectangle_array[j] = 0
                else: 
                    rectangle_array[j] += input_array[i][j]
            answer = max(answer, self.largestRectangleHistogram(rectangle_array))
        return answer



s1 = Solution()
input_array = [[1,0,1,0,0],
                [1,0,1,1,1],
                [1,1,1,1,1],
                [1,0,0,1,0]]
print(s1.solve(input_array))