# https://leetcode.com/problems/top-k-frequent-elements/submissions/
# To find top K frequent numbers we store the frequency of element in heap with their value
# To find frequency we use hash maps
import heapq
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, obj_value2):
        return self.key < obj_value2.key


def solve(input_array, K):
    maps = {}
    for x in input_array:
        if maps.get(x) is None:
            maps[x] = 1
        else:
            maps[x] += 1
    
    i = 0
    heap = []
    for key in maps:
        if i < K:
            heapq.heappush(heap, Item(maps[key], key))
        else:
            heapq.heappushpop(heap, Item(maps[key], key))
        i += 1
    output = []
    while heap:
        output.append(heapq.heappop(heap).value)
    return output

input_array = [1,1,1,2,2,3]
K = 2
print(solve(input_array, K))