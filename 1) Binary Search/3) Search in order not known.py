def binarySearch(input_array, element_to_search):
    n = len(input_array)
    if n == 0:
        return -1
    if n == 1:
        return 0 if input_array[0] == element_to_search else -1
    
    order_type = 'desc' if input_array[0] > input_array[1] else 'asc'

    start = 0
    end = n - 1

    while(start <= end):
        mid = start + (end-start)//2

        if input_array[mid] == element_to_search:
            return mid
        elif order_type == 'asc':
            if input_array[mid] > element_to_search:
                end = mid - 1
            else:
                start = mid + 1
            # For the order_type desc
        else:
            if input_array[mid] > element_to_search:
                start = mid + 1
            else:
                end = mid - 1
    return -1

# Input params
# Sort direction of input_array can be asc or desc
# input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
input_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
element_to_search = 9

print(binarySearch(input_array, element_to_search))