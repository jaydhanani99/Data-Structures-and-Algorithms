# https://leetcode.com/problems/search-a-2d-matrix/
# https://www.interviewbit.com/problems/matrix-search/
# @param input_array : list of list of integers
# @param element_to_search : integer
# @return an integer (1 if element found and 0 if not found)
def search(input_array, element_to_search):
    # Given that 
        # 1) Integers in each row are sorted from left to right.
        # 2) The first integer of each row is greater than or equal to the last integer of the previous row.

    # If we observe the array we can say that if we merge all the rows we have one fully sorted array
    r = len(input_array)
    c = len(input_array[0])
    # now we can declare start as 0 and end as r*c-1
    # However we need to build logic so that we can access index of array in terms of r and c
    # Let's say  if we need to access 7th element (index = 6) of merged array we need to write input_array[1][2]
    # So the general formula will be input_array[index//c][index%c]
    # let's apply binary search in merged array

    start = 0
    end = r*c-1


    while start <= end:
        mid = start + (end-start)//2
        if input_array[mid//c][mid%c] == element_to_search:
            return 1
        elif input_array[mid//c][mid%c] < element_to_search:
            start = mid + 1
        else:
            end = mid - 1
    return 0

input_array = [[1,   3,  5,  7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]]
element_to_search = 30
print(search(input_array, element_to_search))