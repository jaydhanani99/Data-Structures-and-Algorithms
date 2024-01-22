# Given an unsorted array and two numbers x and k, find k closest values to x.
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, obj_value2):
        return self.key < obj_value2.key
import heapq
def solve(input_array, K, input_element):
    # To find K closest we will store the absolute difference between all the array element and input_element in min heap of size K
    # so at last we can have K elements which is closest to input_element
    # To do so we need to store the key value pairs to heap
    # In python we can store class object in heap with __lt__ method in class
    # __lt__ method will be called automatically by heap
    # We need to use max heap to get smallest values at last or we can say closest value at last
    n = len(input_array)
    heap = []
    for i in range(n):
        if i < K:
            # To use maxheap we have inserted negative 
            heapq.heappush(heap, Item(-abs(input_array[i]-input_element), input_array[i]))
        else:
            heapq.heappushpop(heap, Item(-abs(input_array[i]-input_element), input_array[i]))
    output = []
    while heap:
        output.append(heapq.heappop(heap).value)
    return output

input_array = [10, 2, 14, 4, 7, 6]
input_element = 5
K = 3
print(solve(input_array, K, input_element))

