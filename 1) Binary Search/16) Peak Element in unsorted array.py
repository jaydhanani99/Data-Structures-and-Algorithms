# https://www.youtube.com/watch?v=OINnBJTRrMU&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=17
# https://leetcode.com/problems/find-peak-element/
def findPeakElement(input_array):
    n = len(input_array)
    if n == 1:
        return input_array[0]

    # Check for edge element whether it is peak element or not
    if input_array[0] > input_array[1]:
        return  input_array[0]
    if input_array[-1] > input_array[-2]:
        return  input_array[-1]
    
    # Applying binary search on answer concept
    start = 1
    end = n - 2

    while start <= end:
        mid = start + (end-start)//2

        if input_array[mid] > input_array[mid-1] and input_array[mid] > input_array[mid+1]:
            return input_array[mid]
        elif input_array[mid] < input_array[mid+1]:
            start = mid + 1
        else:
            end = mid - 1


input_array = [5, 10, 20, 15]
print(findPeakElement(input_array))