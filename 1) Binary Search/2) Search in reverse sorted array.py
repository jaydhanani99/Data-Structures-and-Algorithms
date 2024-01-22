def binarySearch(input_array, element_to_search):
    n = len(input_array)

    if n == 0:
        return -1
    
    start = 0
    end = n-1

    while start <= end:
        mid = start + (end-start)//2
        if input_array[mid] == element_to_search:
            return mid
        elif input_array[mid] < element_to_search:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# Input params
input_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
element_to_search = 5

print(binarySearch(input_array, element_to_search))