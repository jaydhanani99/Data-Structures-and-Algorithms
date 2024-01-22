# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, string: str) -> str:
        vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        
        n = len(string)
        string = list(string)
        
        start = 0
        end = n - 1
        
        while start < end:
            while start < end and string[start].lower() not in vowels:
                start += 1
            while end > start and string[end].lower() not in vowels:
                end -= 1

            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1
        return ''.join(string)