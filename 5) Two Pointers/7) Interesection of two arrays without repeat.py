# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        
        i = 0
        j = 0
        output = []
        
        # Sorting the array
        nums1.sort()
        nums2.sort()
        
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                output.append(nums1[i])
                # Skipping the same elements
                while i < n1-1 and nums1[i] == nums1[i+1]:
                    i += 1
                while j < n2-1 and nums2[j] == nums2[j+1]:
                    j += 1
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return output