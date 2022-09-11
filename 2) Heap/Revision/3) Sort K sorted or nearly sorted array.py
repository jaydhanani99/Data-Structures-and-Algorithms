# K sorted array means values that should be at index i in sorted array, is available at either i-K or i+K index.
# so basically we will use min heap of size K when the heap size exceed we pop element which is the minimum element so far.
import heapq
# heapq is min heap so when we pop it will return minimum element from array
def solve(input_array, K):
    n = 0
    heap = []
    output = []
    for x in input_array:
        if n < K:
            heapq.heappush(heap, x)
        else:
            output.append(heapq.heappushpop(heap, x))
    
    while heap:
        output.append(heapq.heappop(heap))
    return output


input_array = [6, 5, 3, 2, 8, 10, 9]
K = 3
print(solve(input_array, K))