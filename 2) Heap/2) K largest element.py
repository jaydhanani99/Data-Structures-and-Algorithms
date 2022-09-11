import heapq
# heapq is min heap so when we pop it will return minimum element from array
def solve(input_array, k):
    heap = []
    n = len(input_array)
    for i in range(n):
        if i < k:
            heapq.heappush(heap, input_array[i])
        else:
            heapq.heappushpop(heap, input_array[i])
    return heap

input_array = [7, 10, 4, 3, 20, 15]
k = 1
print(solve(input_array, k))