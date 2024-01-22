# https://leetcode.com/problems/subsets-ii/submissions/

class Solution:
    def __init__(self):
        self.ans    =   []
    def solve(self, input, output):
        if len(input) == 0:
            self.ans.append(output)
            return
            
        # Considering first element in output
        self.solve(input[1::], output+[input[0]])
        
        # Not considering first element in output
        self.solve(input[1::], output)
        
    def subsetsWithDup(self, A):
        A.sort()
        # For better explanation see https://leetcode.com/problems/subsets/
        input = A
        output = []
        
        map = {}
        new_ans = []
        
        self.solve(input, output)
        for x in self.ans:
            current_string = ''.join(str(e) for e in x)
            if map.get(current_string) is None:
                new_ans.append(x)
            map[current_string] = 1
        
        return new_ans