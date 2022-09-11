# https://leetcode.com/problems/intersection-of-two-arrays/


class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # Simple approach by set intersection
        # set1 = set(nums1)
        # set2 = set(nums2)
        # return list(set2 & set1)
    
        # Using manual set intersection
        # set1 = set(nums1)
        # set2 = set(nums2)
        # return self.set_intersection(set1, set2)
        
        
        # Without using set
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