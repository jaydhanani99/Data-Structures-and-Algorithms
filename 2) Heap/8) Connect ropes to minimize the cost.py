# https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
import heapq
def solve(input_array):
    # If we start connecting minimum numbers then total cost would be minimize
    # Because maximum length rope will be added minimum times
    ans = 0
    heapq.heapify(input_array)

    while len(input_array) > 1:
        # connecting first minimum and second minimum rope and adding their cost to ans
        # after connecting rope we will push this rope to input_array for futher connect
        current_connected_rope = heapq.heappop(input_array)+heapq.heappop(input_array)
        # adding cost for current_connected_rope
        ans += current_connected_rope

        # Adding connected rope for further connection
        heapq.heappush(input_array, current_connected_rope)
    return ans


input_array = [ 4, 3, 2, 6 ]
print(solve(input_array))