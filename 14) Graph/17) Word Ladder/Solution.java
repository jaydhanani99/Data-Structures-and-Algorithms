// https://leetcode.com/problems/word-ladder/
// https://www.interviewbit.com/old/problems/word-ladder-i/
// https://practice.geeksforgeeks.org/problems/word-ladder/1/


class Item {
    public String word;
    public int visitedCount = 0;
    public Item(String word, int visitedCount) {
        this.word = word;
        this.visitedCount = visitedCount;
    }
}
class Solution {
    public int ans = Integer.MAX_VALUE;

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        // Creating traverseList this would create hashmap of {srcWord: [all the possible destWord]}
        HashMap<String, HashSet<String>> traverseList = prepareTraversable(beginWord, wordList);
        
        // To keep track of already traversed words
        HashSet<String> visited = new HashSet<>();
        
        // Traversing using BFS
        Queue<Item> q = new LinkedList<>();
        q.add(new Item(beginWord, 1));
        
        while (q.size() > 0) {
            Item current = q.poll();
            if (visited.contains(current.word)) continue;
            visited.add(current.word);
            if (current.word.equals(endWord)) {
                this.ans = Math.min(this.ans, current.visitedCount);
            }

            // Putting all the traversable element in queue by increamenting visitedCount
            Iterator<String> it = traverseList.get(current.word).iterator();
            while (it.hasNext()) {
                String next = it.next();
                // System.out.println("src="+current.word+", dest="+next+", endWord="+endWord+(next.equals(endWord)));
                q.add(new Item(next, current.visitedCount+1));
            }
        }
        return this.ans != Integer.MAX_VALUE ? this.ans : 0;
    }

    public boolean checkDiff(String word1, String word2) {
        int n = word1.length();
        int diff = 0;
        for (int i = 0; i < n; i++) {
            if (word1.charAt(i) != word2.charAt(i)) diff++;
            if (diff > 1) return false;
        }
        return diff == 1 ? true : false;
    }
    
    public HashMap<String, HashSet<String>> prepareTraversable(String beginWord, List<String> wordList) {
        HashMap<String, HashSet<String>> traverseList = new HashMap<String, HashSet<String>>();
        wordList.add(beginWord);
        int n = wordList.size();
        for (int i = 0; i < n; i++) {
            traverseList.put(wordList.get(i), new HashSet<String>());
        }
        for (int i = 0; i < n; i++) {            
            for (int j = i+1; j < n; j++) {
                if (checkDiff(wordList.get(i), wordList.get(j))) {
                    // Adding both in each other list
                    traverseList.get(wordList.get(i)).add(wordList.get(j));
                    traverseList.get(wordList.get(j)).add(wordList.get(i));
                }
            }
        }
        return traverseList;
    }
}