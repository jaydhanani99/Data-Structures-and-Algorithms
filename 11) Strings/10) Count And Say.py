# https://leetcode.com/problems/count-and-say/submissions/
# https://www.interviewbit.com/old/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        string = "1"
        
        while i < n:
            string_len = len(string)
            new_string = []
            # Initially taking first char count as 1
            count = 1
            # storing first char of current string in prev_char
            prev_char = string[0]
            
            
            # Traversing through current string
            for j in range(1, string_len):
                # incrementing current same chars
                if prev_char == string[j]:
                    count += 1
                else:
                    # after that we add count and the char in new_string
                    new_string.append(str(count))
                    new_string.append(string[j-1])
                    prev_char = string[j]
                    count = 1
            
            # Adding last char and it's count
            new_string.append(str(count))
            new_string.append(string[-1])
            
            # Reassing new string to string
            string = ''.join(new_string)
            i += 1
        return string