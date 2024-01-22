# https://www.interviewbit.com/old/problems/implement-strstr/
# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        if needle_length == 0:
            return 0
        n = len(haystack)
        j = 0
        i = 0
        while i < n:
            if haystack[i] == needle[j]:
                # When match occures increase the both the pointer
                i += 1
                j += 1
                # if j == needle_length that means we have encountered the needle
                if j == needle_length:
                    return i-needle_length
            else:
                # else we start from last unmatched index
                i = i - j + 1
                j = 0
        return -1