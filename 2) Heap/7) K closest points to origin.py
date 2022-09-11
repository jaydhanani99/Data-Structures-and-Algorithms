# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq, math
class Item:
    def __init__(self, distance, points):
        self.distance = distance
        self.points = points
    
    def __lt__(self, obj_value2):
        return self.distance < obj_value2.distance



def solve(input_points, k):
    # Here we need to find the k points which are closest to the origin
    # To find the distance between two points is sqrt((x1-x2)^2 + (y1-y2)^2)
    # however here we have x1 and y1 as zero which is the origin
    # so our formula is sqrt((x2)^2 + (y2)^2)
    # so basically we need to store this as our heap key and point array as value
    # so we will create Item class based on this

    i = 0
    heap = []
    for x in input_points:
        # Here we need to use max heap to keep minimum values in heap so we are storing negative values in heap
        if i < k:
            heapq.heappush(heap, Item(-math.sqrt((x[0]**2 + x[1]**2)), x))
        else:
            heapq.heappushpop(heap, Item(-math.sqrt((x[0]**2 + x[1]**2)), x))
        i += 1
    
    output = []
    while heap:
        output.append(heapq.heappop(heap).points)
    return output
input_points = [[3,3],[5,-1],[-2,4]]
k = 2
print(solve(input_points, k))