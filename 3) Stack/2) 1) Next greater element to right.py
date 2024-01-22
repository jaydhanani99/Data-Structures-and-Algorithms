# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1
# https://www.youtube.com/watch?v=NXOOYYwpbg4&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=2

class Solution:
    def solve(self, input_array):
        # Here brute force solution would be O(n^2)
        # So we can identify that this problem is related to stack
        # The idea is we store the current greater elements in stack
        # To do so we start traversing array from reverse order
        # On next iteration we pop the elements from stack until we found the greater element
        # if stack becomes empty we store -1 in output array else we store top element in output array
        # At last we have our answer in output array in reverse order
        # so we return by reversing it
        answer = []
        stack = []
        n = len(input_array)

        for i in range(n-1, -1, -1):
            # We pop element till we found the element greater than the current element
            while stack and stack[-1] <= input_array[i]:
                stack.pop()

            if stack:
                # If we found greater element than current element we store that element in answer
                answer.append(stack[-1])
            else:
                # If stack becomes empty that means no greater element is exists so we store the -1 in answer
                answer.append(-1)             

            # At last we push the current element to stack
            stack.append(input_array[i])
        # Returning reversed answer as we have answer in reverse order
        return answer[::-1]


input_array = [1, 3, 2, 4]
s1 = Solution()
print(s1.solve(input_array))