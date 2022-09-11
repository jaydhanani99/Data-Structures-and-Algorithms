# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
# https://www.interviewbit.com/problems/rotated-sorted-array-search/
def binarySearch(arr, element_to_search):
    n = len(arr)
    if n == 0:
        return -1
    start = 0
    end = n - 1

    while start <= end:
        mid = start + (end - start)//2

        if arr[mid] == element_to_search:
            return mid
        elif arr[mid] < element_to_search:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def solve(input_array, element_to_search):
    # First we will find the minimum element in rotated sorted array
    # After finding minimum element we will search in both sorted array which is start, min-1 and min, end

    n = len(input_array)
    if n == 0:
        return -1

    start = 0
    end = n - 1
    min_index = 0
    # Finding minimum element index
    while start <= end:
        mid = start + (end-start)//2

        if input_array[(mid-1+n)%n] > input_array[mid] and input_array[(mid+1)%n] > input_array[mid]:
            min_index = mid
            break
        elif input_array[end] < input_array[mid]:
            start = mid + 1 
        else:
            end = mid - 1
    
    # Applying binary search in both part of array and return the maximum index bcz one should return correct index and other should -1
    left_result = binarySearch(input_array[0:min_index], element_to_search)
    if left_result != -1:
        return left_result

    right_result = binarySearch(input_array[min_index:n], element_to_search)
    if right_result != -1:
        # Adding length of left sub array
        return right_result+min_index
    return -1

input_array = [1,3]
element_to_search = 1
print(solve(input_array, element_to_search))