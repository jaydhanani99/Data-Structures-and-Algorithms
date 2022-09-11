# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def binarySearch(input_array):
    # To find number of time array is rotated we need to find the minimum element in array
    # However our array is not fully sorted we have two separate sub array which are sorted
    # for example 11, 12, 15, 18, 2, 5, 6, 8 minimum element is 2 and the number of time array is rotated is index of 2 which is 4
    # Here two sub array 11, 12, 15, 18 and 2, 5, 6, 8 is sorted sub array
    # Here left element and right element of minimum element are greater than it (18 and 5 are greater than 2)
    # so if we found mid element which is smaller than their adjancents we will get our answer
    # in our example initially start is 11 and end is 8 and mid is 18
    # now our task is to choose the direction either left or right
    # for the mid element we need to identify unsorted sub array which is either 11, 12, 15, 18 or 18, 2, 5, 6, 8 
    #   in our case it is 18, 2, 5, 6, 8
    # so based on mid & start or mid & end we identify unsorted array and choose start/end accordingly
    n = len(input_array)

    # Handling base cases
    if n <= 1:
        return 0
    if n == 2:
        return 0 if input_array[0] < input_array[1] else 1


    start = 0
    end = n - 1

    while start <= end:
        mid = start + (end-start)//2
        # here %n is for the edge elements which is either at 0 index or (n-1)th index
        if input_array[(n+mid-1)%n] > input_array[mid] and input_array[(mid+1)%n] > input_array[mid]:
            return mid
        elif input_array[end] < input_array[mid]:
            start = mid + 1
        else:
            # We need to put end = mid - 1 in else condition because our aim is to find the smallest element which will rely on left sub array if array is sorted
            # if we put start = mid + 1 in else condition our code will fail in some testcases like 11, 12, 15, 18, 2, 5, 6, 8
                # because when we have mid = 18 we have start 11 and end 8 and our if condition input_array[start] > input_array[mid] will fail
                # at that time we set start as 2 and end as 8 and for subsequent call we will move right side of the array so we miss our ans which is 2
            # Another reason is if we have whole sorted array we always go right side but we should in left side
            # That's the reason we need to go left in else condition    
            end = mid - 1
    return 0



input_array = [11, 12, 15, 18, 2, 5, 6, 8]
print(binarySearch(input_array))