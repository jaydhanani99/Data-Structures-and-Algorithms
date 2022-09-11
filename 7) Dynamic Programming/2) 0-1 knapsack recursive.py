# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.youtube.com/watch?v=kvyShbFVaY8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=3
# https://www.interviewbit.com/problems/0-1-knapsack/

class Solution:
#                                 # profit (Remaining Capacity) (current answer which is maximum of both child)
#                                                                     0 (5)(220)
#                                                  /                                             \
#                                                 /                                               \
# n = 0                           (including profit of n = 0)60(4)(180)   (not including profit for n = 0) 0(5)(220)
#                                      /                    \                              /               \
#                                     /                      \                            /                 \
# n = 1                           160(2)(160)               60(4)(180)              100(3)(220)           0(5)(120)
#                             /               \           /           \             /         \           /       \
#                            /                 \         /             \           /           \         /         \
# n = 2                   160(2)(160)   160(2)(160) 180(1)(180)      60(4)(60) 220(2)(220) 100(3)(100) 120(2)(120) 0(5)(0)

    def solve(self, weight, value, W, n):
        # Base condition
            # 1) n == 0 means we do not have item left to put in bag
            # 2) W == 0 means we have filled all the space of bag
        if n == 0 or W == 0:
            return 0

        # if last item weight is less then the remaining size of bag
        if weight[n-1] <= W:
            # Then we have two options either include current item or not include
            # Including the last item (update the remaining bag size and n as n-1 for last item in next iteration)
            # Or not including the current item 
            #       (as we have not included the item we do not update the remaining bag size, and n as n-1 for last item in next iteration)

            # We return maximum of both the possibility
            return max((value[n-1]+self.solve(weight, value, W-weight[n-1], n-1)), 
                        (self.solve(weight, value, W, n-1)))
        
        # If current item weight is greater than the remaining bag size we do not include the current item
        return self.solve(weight, value, W, n-1)


    # should return maximum profit
    def knapsack(self, weight, value, W):
        return self.solve(weight, value, W, len(weight))









sol = Solution()
# Weight of item
weight = [1, 2, 3]

# Profit of item
value = [60, 100, 120]

# capacity of bag
W = 5
print(sol.knapsack(weight, value, W))