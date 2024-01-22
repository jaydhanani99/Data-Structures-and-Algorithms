# https://www.interviewbit.com/problems/search-for-a-range/
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
def getElementOccurance(input_array, element_to_search, start, end, occurance_type='first'):
    current_occurance = - 1
    while(start <= end):
        mid = start + (end-start)//2

        if input_array[mid] == element_to_search:
            current_occurance = mid
            # further search on left sub array to find first occurance
            if occurance_type == 'first':
                end = mid - 1
            # further search on right sub array to find last occurance
            else:
                start = mid + 1
        elif input_array[mid] > element_to_search:
            end = mid - 1
        else:
            start = mid + 1
    return current_occurance
def binarySearch(input_array, element_to_search):
    n = len(input_array)
    if n == 0:
        return -1,-1
    
    start = 0
    end = n - 1

    # Finding first occurance
    first_occurance = getElementOccurance(input_array, element_to_search, start, end, 'first')
    last_occurance = getElementOccurance(input_array, element_to_search, start, end, 'last')

    return first_occurance, last_occurance


input_array = [1, 2, 3, 9, 9, 9, 10, 11, 12]
element_to_search = 9

print(binarySearch(input_array, element_to_search))