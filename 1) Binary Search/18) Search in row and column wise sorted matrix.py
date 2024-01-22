# https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/
def search(input_array, element_to_search):
    r = len(input_array)
    c = len(input_array[0])

    # We start searching from top right corner if element is greater than the input element we increase the i
    # if element is smaller than input element we decrease the j
    i = 0
    j = c - 1

    while i < r and j >= 0:
        if input_array[i][j] == element_to_search:
            return True
        elif input_array[i][j] > element_to_search:
            j = j - 1
        else:
            i = i + 1
    return False 


input_array = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
element_to_search = 27
print(search(input_array, element_to_search))