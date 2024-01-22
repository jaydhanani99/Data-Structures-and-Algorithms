# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Using extra space and without using sorting
        dict1 = {}
        dict2 = {}
        
        for x in nums1:
            if x in dict1:
                dict1[x] += 1
            else:
                dict1[x] = 1
        for x in nums2:
            if x in dict2:
                dict2[x] += 1
            else:
                dict2[x] = 1
        output = []
        # Traversing in one dict         
        for key in dict1:
            # if key is available in dict2 then we add this number min(dict1, dict2) times
            if key in dict2:
                number_count = min(dict1[key], dict2[key])
                output.extend([key]*number_count)
        return output
        
        
        
        # Without using extra space and using sorting
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
                # # Skipping the same elements
                # while i < n1-1 and nums1[i] == nums1[i+1]:
                #     i += 1
                # while j < n2-1 and nums2[j] == nums2[j+1]:
                #     j += 1
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return output