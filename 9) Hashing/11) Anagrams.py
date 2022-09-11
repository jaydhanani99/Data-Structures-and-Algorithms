# https://www.interviewbit.com/old/problems/anagrams/

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, strings):
        dict = {}
        n = len(strings)
        ans = []
        ansIndex = 0
        for i in range(n):
            current_sorted_string = ''.join(sorted(strings[i]))
            if current_sorted_string in dict:
                ans[dict[current_sorted_string]].append(i+1)
            else:
                dict[current_sorted_string] = ansIndex
                ansIndex += 1
                ans.append([i+1])
        return ans