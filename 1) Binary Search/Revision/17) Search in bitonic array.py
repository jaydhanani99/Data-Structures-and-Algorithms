# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# https://leetcode.com/problems/find-in-mountain-array
# Bitonic array means first its monotonically increasing order after some point its monotonically decreasing order
def binarySearch(input_array, element_to_search, order = 'asc'):
    n = len(input_array)
    start = 0
    end = n - 1

    while start <= end:
        mid = start + (end-start)//2
        if input_array[mid] == element_to_search:
            return mid
        elif (input_array[mid] > element_to_search and order == 'asc') or (input_array[mid] < element_to_search and order == 'desc'):
            end = mid - 1
        else:
            start = mid + 1
    return -1

def searchInBitonic(input_array, element_to_search):
    # first we will identify peak element in bitonic array
    n = len(input_array)

    if n == 1:
        return 0 if input_array[0] == element_to_search else -1

    # Check for edge element whether it is peak element or not
    peak_element_index = - 1
    if input_array[0] > input_array[1]:
        peak_element_index = 0
    if input_array[-1] > input_array[-2]:
        peak_element_index = n - 1

    start = 1
    end = n - 2
    # finding peak element in bitonic array
    while start <= end:
        mid = start + (end-start)//2
        if input_array[mid] > input_array[mid+1] and input_array[mid] > input_array[mid-1]:
            peak_element_index = mid
            # if peak element is the element_to_search directly returning from here
            if input_array[peak_element_index] == element_to_search:
                return mid
            break
        elif input_array[mid+1] > input_array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    # After finding peak element index we will apply binary search in both halves of the array
    # Applying on left half
    left_half_search_index = binarySearch(input_array[0:peak_element_index], element_to_search, 'asc')
    if left_half_search_index != -1:
        return left_half_search_index
    
    # Applying on right half
    right_half_search_index = binarySearch(input_array[peak_element_index:n], element_to_search, 'desc')
    if right_half_search_index != -1:
        return peak_element_index+right_half_search_index
    return -1
input_array = [ 1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 2 ]
element_to_search = 5
print(searchInBitonic(input_array, element_to_search))