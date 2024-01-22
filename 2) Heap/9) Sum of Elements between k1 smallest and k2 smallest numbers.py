# https://www.geeksforgeeks.org/sum-elements-k1th-k2th-smallest-elements/
# https://practice.geeksforgeeks.org/problems/sum-of-elements-between-k1th-and-k2th-smallest-elements3133/1#
import heapq
def solve(a, n, k1, k2):
    # sorting k1 and k2 to find k1th smallest and k2th smallest element
    if k1 > k2:
        k1, k2 = k2, k1

    heapq.heapify(a)
    ans = 0
    prev_x = -1
    nth_smallest = 0
    while a:
        x = heapq.heappop(a)
        if x != prev_x:
            nth_smallest += 1
        
        if nth_smallest > k1 and nth_smallest < k2:
            ans += x
        if nth_smallest >= k2:
            break
        prev_x = x
    return ans



a = [3, 1, 7, 7, 8, 9, 5, 5, 10]
k1 = 10
k2 = 5
n = len(a)
print(solve(a, n, k1, k2))