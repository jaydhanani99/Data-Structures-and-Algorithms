def binarySearch(input_array, element_to_search):
    n = len(input_array)
    if n == 0:
        return -1
    
    start = 0
    end = n - 1
    # Nearly sorted array means element that should be at ith index that can be at ith or (i-1)th or at (i+1)th index.
    # so basically we will check mid, mid - 1 and mid + 1 with the element bcz element can be at any position described.
    # if element not found at given position we will either move to mid - 2 or mid + 2 based on the element value
    while start <= end:
        mid = start + (end - start)//2

        if (mid - 1 >= start and input_array[mid - 1] == element_to_search):
            return mid - 1
        elif (mid + 1 <= end and input_array[mid + 1] == element_to_search):
            return mid + 1
        elif (input_array[mid] == element_to_search):
            return mid
        elif input_array[mid] >= element_to_search:
            end = mid - 2
        else:
            start = mid + 2
    return -1


input_array = [2, 1, 4, 3, 6, 5, 8, 7, 9]
element_to_search = 9

print(binarySearch(input_array, element_to_search))