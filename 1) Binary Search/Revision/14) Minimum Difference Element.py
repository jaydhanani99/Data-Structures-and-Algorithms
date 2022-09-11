def binarySearch(input_array, input_element):
    n = len(input_array)

    start = 0
    end = n - 1

    while start <= end:
        mid = start + (end-start)//2
        if  input_array[mid] == input_element:
            return 0
        if input_array[mid] > input_element:
            end = mid - 1
        else:
            start = mid + 1
    # if start or end is overflow in case of last iteration
    if start > n - 1:
        start = n - 1
    if end < 0:
        end = 0
    # After the binary search operation our start and end points near to the input_element
    return min(abs(input_array[start] - input_element), abs(input_array[end] - input_element))

input_array = [5, 15, 67, 89, 90, 110]
input_element = 500

print(binarySearch(input_array, input_element))