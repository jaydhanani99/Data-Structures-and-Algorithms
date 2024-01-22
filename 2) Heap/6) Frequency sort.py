# https://leetcode.com/problems/sort-array-by-increasing-frequency/submissions/
import heapq
class Item:
    def __init__(self, frequency, value):
        self.frequency = frequency
        self.value = value
    def __lt__(self, obj_value2):
        # Returning item based on the frequency and if frequency is the same then returning based on the value as per the problem definition
        if self.frequency < obj_value2.frequency:
            return True
        elif self.frequency == obj_value2.frequency and self.value > obj_value2.value:
            return True
        else:
            return False

def solve(input_array):
    # Creating maps to store the frequency of the element
    maps = {}
    for x in input_array:
        if maps.get(x) is None:
            maps[x] = 1
        else:
            maps[x] += 1
            
    heap = []
    # Pushing element based on the frequency in heap
    for x in maps:
        heapq.heappush(heap, Item(maps[x], x))
        
    output = []

    # Retrieving elements from heap based on the frequency and storing then into output variable as per their frequency
    while heap:
        item = heapq.heappop(heap)
        output.extend([item.value for i in range(item.frequency)])

    return output

input_array = [1,1,2,2,2,3]
print(solve(input_array))