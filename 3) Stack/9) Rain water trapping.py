# https://www.interviewbit.com/problems/rain-water-trapped/
# https://www.youtube.com/watch?v=FbGG2qpNp4U&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=9
# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def solve(self, input_array):
        # To find the trapped water we can calculated trapped water on each pillar
        # To find the trapped water on each pillar we just need to find maximum pillar size in left and right of current pillar
        # By doing so we can simpley do min(max_left_pillar, max_right_pillar) - current_pillar
        #   and we do some for each pillar
        n = len(input_array)
        right_max_pillars = [0]*n

        current_max = input_array[-1]
        for i in range(n-1, -1, -1):
            current_max = max(current_max, input_array[i])
            right_max_pillars[i] = current_max

        current_max = input_array[0]
        answer = 0
        for i in range(n):
            current_max = max(current_max, input_array[i])
            answer += (min(right_max_pillars[i], current_max)-input_array[i])
        return answer


        # The most efficient approach of this problem is two pointer approach.
        # O(N) time and O(1) space complexity
        # we assign left as 0 and left_max as A[0] same way right as len(A) - 1 and right_max as A[-1]
        if len(input_array) == 0:
            return 0
        left        =   0
        left_max    =   input_array[0]
        right       =   len(input_array) - 1
        right_max   =   input_array[-1]
        ans         =   0
        while(left < right):
           # Now we check if right wall is larger than the left wall
            if input_array[left] < input_array[right]:
                # if so we check if current left wall is larger than the all time maximum of left(left_max)
                if input_array[left] >= left_max:
                   # if so we update the left_max
                    left_max    =   input_array[left]
                else:
                   # if not that means some amount of water will be trapped on current wall, so we update the ans.
                    ans         +=  (left_max - input_array[left])
                left            +=  1
            else:
               # Else either both wall is same or the left wall is larger than the right wall.
               #And we check if right wall is larger than the all time maximum of the right(right_max)
                if input_array[right] > right_max:
                   # if so we update the right_max
                    right_max    =   input_array[right]
                else:
                   # if not that means some amount of water will be trapped on current wall, so we update the ans.
                    ans          +=  (right_max - input_array[right])
                right           -=  1
        return ans




s1 = Solution()
input_array = [3, 0, 0, 2, 0, 4]
print(s1.solve(input_array))