# https://leetcode.com/problems/search-insert-position/
# https://www.interviewbit.com/problems/sorted-insert-position/
def searchInsertPosition(input_array, input_element):
    # This problem is same as floor value problem we just need to find floor value position and return position+1
    n = len(input_array)
    start = 0
    end = n - 1
    floor_index = -1
    while start <= end:
        mid = start + (end-start)//2
        
        if input_array[mid] == input_element:
            return mid
        elif input_array[mid] < input_element:
            start = mid + 1
            floor_index = mid
        else:
            end = mid - 1
    return floor_index+1

input_array = [1,3,5,6]
input_element = 5
print(searchInsertPosition(input_array, input_element))