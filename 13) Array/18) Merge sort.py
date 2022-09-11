# https://leetcode.com/problems/sort-an-array/

# Merge Sort:
#     Comparison based algorithm with running time complexity O(N logN)
#     It is stable algorithm.
#     Although heapsort has the sme time bounds as merge sort -> heapsort requires only theta(1) auxiliary space instead of merge sorts theta(n)(theta means we cannot de better than O(n) space complexity
#     Efficient quicksort implementations generally outperforms mergesort.
#     As far as java is concern merge sort for sorting the referencedd types and uses quicksort for sorting primitive types such as int, char...
#     Merge sort is often the best choice for sorting the linked list: 
#         -> in this situation it is relatively easy to implement a merge sort in such a way that it requires only theta(1) extra space.
    
#     Comparison of quicksort and merge sort.
#                         quicksort           mergesort
#         In place            Yes                 No
#         stable              No                  Yes
#         Time Complexity     O(N2) sometimes     O(N logN)

#     Algorithm:
#         1) Divide the array into two subarrays recursively
#         2) Sort these subarrays recursively with mergesort again
#         3) If there is only a single item left in the subarray
#             -> we consider it to be sorted by definition
#         4) merge the subarrays to get the final sorted array.

class Solution:
    def merge(self, left, right):
        # So let's say we at second last merge position
        # At this point both half contain half of the array element.
        # e.g. we have two half [1, 2, 4, 6] and [3, 5, 7, 8]
        # so compare each element of both half and stores smaller one and increament that index
        # at last it may be possible that any of one half contain elements at that time we simply concat it
        ans = []
        
        i = 0
        j = 0
        
        left_n = len(left)
        right_n = len(right)
        
        while i < left_n and j < right_n:
            if left[i] < right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        # Storing left half remaining element if exist
        ans.extend(left[i:])
        # Storing right half remaining element if exist
        ans.extend(right[j:])
        return ans
        
    def partition(self, nums):
        n = len(nums)
        if n == 1:
            return nums
        
        # First we break our array into two halves
        # It will break the array recursively until left and right half contain only one element.
        # when it contain only one element it starts merging it using function merge
        left = nums[:n//2]
        right = nums[n//2:]
        
        left = self.partition(left)
        right = self.partition(right)
        
        # Now when all the array are broke we will start merging it
        return self.merge(left, right)
        
    
    def sortArray(self, nums: List[int]) -> List[int]:
        # Using merge sort
        return self.partition(nums)