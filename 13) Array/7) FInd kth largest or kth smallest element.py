# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1#
# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, input_array: List[int], k: int) -> int:
        # so basically we are traversing n elements
        # and for each element heap is taking logk time complexity to reconstruct the heap where k is the number element present in heap
        # so overall time complexity will O(nlogk) which is lower than the O(nlogn)
        # So if we sort the array  time complexity would be O(nlogn) which is reduced using heap to O(nlogk)
        heap = []
        n = len(input_array)
        for i in range(n):
            if i < k:
                heapq.heappush(heap, input_array[i])
            # Once the heap size is greater than the k we start poping smallest element from heap and inserting current element
            # as we only required k element from which we need largest
            else:
                heapq.heappushpop(heap, input_array[i])
        return heap[0]