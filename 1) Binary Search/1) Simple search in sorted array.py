def binarySearch(input_array, element_to_search):
    n = len(input_array)

    if n == 0:
        return -1

    start = 0
    end = n-1

    while(start <= end):
        mid = start + (end-start)//2

        if input_array[mid] == element_to_search:
            return mid
        elif input_array[mid] < element_to_search:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Input params
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_to_search = 5

print(binarySearch(input_array, element_to_search))