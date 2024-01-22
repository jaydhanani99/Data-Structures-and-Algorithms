# https://www.geeksforgeeks.org/floor-in-a-sorted-array/
def binarySearch(input_array, element_to_search):
    start = 0
    n = len(input_array)
    end = n - 1

    floor_element = - 1
    while start <= end:
        mid = start + (end - start)//2

        if input_array[mid] == element_to_search:
            return element_to_search
        elif input_array[mid] < element_to_search:
            floor_element = input_array[mid]
            start = mid + 1
        else:
            end = mid - 1
    return floor_element

input_array = [21]
element_to_search = 21
print(binarySearch(input_array, element_to_search))