# Similar problems
    # 1) https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
        # => Just use min heap
    

import heapq
# heapq.heapify(array)
# It will pop smallest element in min heap and largest element in max heap
# heapq.heappop(array)
# heapq.heappush(array, element)


def solve(input_array, k):
    # so basically we are traversing n elements
    # and for each element heap is taking logk time complexity to reconstruct the heap where k is the number element present in heap
    # so overall time complexity will O(nlogk) which is lower than the O(nlogn)
    # So if we sort the array  time complexity would be O(nlogn) which is reduced using heap to O(nlogk)
    heap = []
    n = len(input_array)
    for i in range(n):
        if i < k:
            # inserting negative value to construct max heap as heapq is the min heap
            heapq.heappush(heap, -input_array[i])
        # Once the heap size is greater than the k we start poping largest element from heap and inserting current element
        # as we only required k element from which we need smallest
        else:
            heapq.heappushpop(heap, -input_array[i])
    return -heap[0]



input_array = [7, 10, 4, 3, 20, 15]
k = 25
print(solve(input_array, k))