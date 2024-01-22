def binarySearch(input_array, element_to_find_next_alphabet):
    start = 0
    n = len(input_array)
    end = n - 1

    next_alphabet = - 1
    while start <= end:
        mid = start + (end - start)//2
        if input_array[mid] > element_to_find_next_alphabet:
            next_alphabet = input_array[mid]
            end = mid - 1
        else:
            start = mid + 1
    return next_alphabet


element_to_find_next_alphabet = 'a'
input_array = ['a', 'b', 'c', 'e', 'f', 'o']
print(binarySearch(input_array, element_to_find_next_alphabet))