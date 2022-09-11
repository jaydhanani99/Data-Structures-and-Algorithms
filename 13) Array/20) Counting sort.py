# Counting Sort:
#     Integer sorting algorithm.
#     we assume that the values to be integers
#     It's not comparison based algorithm.
#     Running time O(N + k)
#     Where k is max(array) - min(array)  + 1

# How Counting Sort Works
# We create an array say temp_array size of max(input_array) - min(input_array) + 1
# Initialize all the value with 0
# we traverse through input_array on every element we increment value of temp_array[element]
# After traversing input_array we traverse through temp_array and print index x times where x is the value of element.

def count_sort(nums, max_ele, min_ele):
    countArray      =   [0]*(max_ele-min_ele+1)
    for x in nums:
        # As array start with zero
        countArray[x-1]     +=  1
    return_list     =   []
    for i in range(0, len(countArray)):
        return_list +=  countArray[i]*[i+1]
    return return_list
temp_array  =   [2, 1, 6, 7, 8542, 3697]   
print(count_sort(temp_array, max(temp_array), min(temp_array) ))