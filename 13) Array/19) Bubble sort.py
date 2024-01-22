# Bubble Sort:

#     => Repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order.
#     => It is too slwo and impractical for most problems even when compared to insertion sort.
#     => Bubble sort has worst-case and average complexity both O(N2)
#     => Stable sorting algorithm.
#     => In place algorithm does not need any  additional memory.
#     => In computer graphics it is popular for its capability to detect a very small error 
#        like swap of just two eleemnts in almost-sorted arrays and fix it with just 
#        linear complexity O(N).

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        # with every iteration we bubble up the largest item and place at end
        # so we minus i at every iteration because largest item is placed at end and which is it's actual position
        for j in range(0, len(nums) - 1 -i, 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1]  =   nums[j+1], nums[j]
    return nums

# Now we can make it more efficient
# If in inner loop all the time condition gives false that means array is now in sorted order
def bubble_sort2(nums):
    for i in range(len(nums) - 1):
        # with every iteration we bubble up the largest item and place at end
        # so we minus i at every iteration because largest item is placed at end and which is it's actual position
        # Initially we set flag sorted as True
        # if any swap occure then we change it to False
        # After loop complete if we found sorted = True that means all the elements are now in sorted so we break the loop
        # Same trick cant be use in selection sort as we compare first element with all element and store min to first
        sorted  =   True
        for j in range(0, len(nums) - 1 -i, 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1]  =   nums[j+1], nums[j]
                sorted  =   False
        if sorted == True:
            break
        
    return nums

print(bubble_sort2([-78, -9, -2, 6, 8, 15, 98]))