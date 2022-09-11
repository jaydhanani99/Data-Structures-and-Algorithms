# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        index = 0
        ans = []
        for x in strs:
            sorted_str = ''.join(sorted(x))
            
            if sorted_str in dict:
                ans[dict[sorted_str]].append(x)
            else:
                dict[sorted_str] = index
                ans.append([x])
                index += 1
        return ans