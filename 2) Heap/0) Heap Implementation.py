# https://www.youtube.com/watch?v=Q_eia3jC9Ts
def parentIndex(index):
    # parent node = i => left_child = 2*i + 1, right_child = 2*i+2
    # so if child index is i then parent index would be i-1//2
    # we have done //2 so we can get parent for (index-2) and (index-1) both
    return (index-1)//2

def leftIndex(index):
    return 2*index + 1

def rightIndex(index):
    return 2*index + 2

def insert(A, element):
    # This function is used to insert element in heap array
    # Now to insert array we just append the element at last
    # After appending the element at last we check it with parent 
        # if element is greater than parent we swap, so keep doing it until we need to swap
    A.append(element)

    current_index = len(A)-1
    parent_index = parentIndex(current_index)
    while parent_index >= 0 and A[parent_index] < A[current_index]:
        A[parent_index], A[current_index] = A[current_index], A[parent_index]
        current_index = parent_index
        parent_index = parentIndex(current_index)
    
    return A



def max_heapify(A, index, n):
    """Here n is for upto n element we will heapify the array 
        This will be useful in heapsort"""
    # Now to heapify from current index
    # We compare current element with left and right
    # if we found any element which is greater than the current element
    # we swap it and call the heapify for furhter check to their children
    # Initially we assume that current index is the largest index
    largest = index
    left = leftIndex(index)
    right = rightIndex(index)

    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    # That means we need to swap and call heapify for further elements
    if largest != index:
        A[largest], A[index] = A[index], A[largest]
        max_heapify(A, largest, n)

def build_max_heap(A):
    # To build max heap from normal array
    # We need to heapify non leaf elements starting from end
    # Because non leaf node does not contain any children so we cannot decide element is at right position or not
    # Elements that has index greater than (n//2)-1 are leaf nodes
    # So we start heapify process from (n//2)-1 to 0
    # Or we can also start from the parent of last element of array both are the same
    n = len(A)
    start = parentIndex(n-1) # Which actually provides last index of non leaf node
    while start >= 0:
        max_heapify(A, start, n)
        start -= 1
    return A

def heapsort(A):
    # To sort the heap we will swap the first element (which is the maximum element) with last unsorted element
        # and call the heapify for unsorted elements
    # So we will do this for each element start from end to second element as in last iteration first element will be sorted only
    n = len(A)
    for i in range(n-1, 0, -1):
        # Here A[i] is the last unsorted element
        A[i], A[0] = A[0], A[i]
        # Here we are calling max_heapify from root node only not from the last non leaf node
        # The reason behind is we know that after swapping first and last element the problem is in first element only
        # so we call heapify from first element itself
        # We can call from last element but at that point we also need to call for their parents too in for loop 
        # e.g. start = parentIndex(i-1)
        #     while start >= 0
        #         max_heapify(A, start, i)
        #         start -= 1
        # So by passing first index actually we are reducing one for loop
        max_heapify(A, 0, i)
    return A

A = [-11, -2, -9, -13, -57]
A = build_max_heap(A)
print(A)
# [57, 13, 9, 11, 2]
#                 57
#             /         \
#            13         9
#            / \       /
#           9   11     2
        
# A = insert(A, 500)
# A = insert(A, 0)
# A = insert(A, 400)
# # Will print max_heap
# print(A)
# # Will print sorted array
# A = heapsort(A)
# print(A)

