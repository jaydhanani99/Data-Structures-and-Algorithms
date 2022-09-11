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
def solve(input_array, element_to_search):
    start = 0
    end = 1

    while input_array[end] < element_to_search:
        start = end
        end = end * 2
    return binarySearch(input_array[start:end+1], element_to_search)+start

input_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,999999999999]

# Given that
#   1) The size of the array will always more than double than the index of the input element or next greater input element if element does not exists
# You are not allowed to find the length of the array

element_to_search = 4
print(solve(input_array, element_to_search))