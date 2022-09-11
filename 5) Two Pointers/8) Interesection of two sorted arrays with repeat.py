# https://www.interviewbit.com/problems/intersection-of-sorted-arrays/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def intersect(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        
        i = 0
        j = 0
        output = []
        
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                output.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return output