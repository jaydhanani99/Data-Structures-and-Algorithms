# https://www.geeksforgeeks.org/floor-in-a-sorted-array/
def binarySearch(input_array, element_to_search):
    start = 0
    n = len(input_array)
    end = n - 1

    ceil_element = -1
    while start <= end:
        mid = start + (end - start)//2

        if input_array[mid] == element_to_search:
            return element_to_search
        elif input_array[mid] > element_to_search:
            ceil_element = input_array[mid]
            end = mid - 1
        else:
            start = mid + 1
    return ceil_element

input_array = [1,2,3,4,8,10,10,12,19]
element_to_search = 13
print(binarySearch(input_array, element_to_search))