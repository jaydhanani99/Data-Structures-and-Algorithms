# https://practice.geeksforgeeks.org/problems/shortest-unique-prefix-for-every-word/1/#
# https://www.interviewbit.com/problems/shortest-unique-prefix/

class Trie:
    def __init__(self):
        self.count = 0
        self.children = {}
        
class Solution:
    def __init__(self):
        self.trie = Trie()

    def buildTrie(self, arr, N):
        for i in range(N):
            str_len = len(arr[i])
            current_trie = self.trie
            for j in range(str_len):
                if arr[i][j] not in current_trie.children:
                    children = current_trie.children
                    current_trie.children[arr[i][j]] = Trie()
                current_trie.count += 1
                current_trie = current_trie.children[arr[i][j]]
        
    def findPrefixes(self, arr, N):
        # code here
        ans = []
        self.buildTrie(arr, N)
        for i in range(N):
            str_len = len(arr[i])
            current_trie = self.trie
            current_ans = []
            for j in range(str_len):
                if arr[i][j] not in current_trie.children or current_trie.children[arr[i][j]].count < 2:
                    current_ans.append(arr[i][j])
                    ans.append(''.join(current_ans))
                    break
                else:
                    current_ans.append(arr[i][j])
                current_trie = current_trie.children[arr[i][j]]
            
        return ans