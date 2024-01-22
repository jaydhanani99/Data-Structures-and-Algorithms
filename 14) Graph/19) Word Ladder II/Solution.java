// https://leetcode.com/problems/word-ladder-ii/submissions/
// https://www.interviewbit.com/old/problems/word-ladder-ii/
// https://practice.geeksforgeeks.org/problems/word-ladder-ii/1/

class Item {
    public String word;
    public List<String> currentList;
    public int visitedCount = 0;
    public Item(String word, List<String> currentList, int visitedCount) {
        this.word = word;
        this.currentList = currentList;
        this.visitedCount = visitedCount;
    }
}

class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        int minCost = Integer.MAX_VALUE;
        // Creating traverseList this would create hashmap of {srcWord: [all the possible destWord]}
        HashMap<String, HashSet<String>> traverseList = prepareTraversable(beginWord, wordList);
        
        HashMap<Integer, List<List<String>>> pathWithCost = new HashMap<>();
        
        // To keep track of already traversed words
        HashSet<String> visited = new HashSet<>();
        
        // Traversing using BFS
        Queue<Item> q = new LinkedList<>();
        q.add(new Item(beginWord, new ArrayList<>(List.of(beginWord)), 1));
        
        while (q.size() > 0) {
            Item current = q.poll();
            visited.add(current.word);
            if (current.word.equals(endWord)) {
                
                if (pathWithCost.containsKey(current.visitedCount)) {
                    pathWithCost.get(current.visitedCount).add(current.currentList);
                } else {
                    List<List<String>> s = new ArrayList<>();
                    s.add(current.currentList);
                    pathWithCost.put(current.visitedCount, s);
                }
                minCost = Math.min(minCost, current.visitedCount);
            }

            // Putting all the traversable element in queue by increamenting visitedCount
            Iterator<String> it = traverseList.get(current.word).iterator();
            while (it.hasNext()) {
                String next = it.next();
                // System.out.println("src="+current.word+", dest="+next+", endWord="+endWord+(next.equals(endWord)));
                
                if (!visited.contains(next)) {
                    List<String> nextList = new ArrayList<>(current.currentList);
                    nextList.add(next);
                    q.add(new Item(next, nextList, current.visitedCount+1));
                }
            }
        }
        return pathWithCost.containsKey(minCost) ? pathWithCost.get(minCost) : new ArrayList<>();
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
        int n = wordList.size();
        for (int i = 0; i < n; i++) {
            traverseList.put(wordList.get(i), new HashSet<String>());            
            for (int j = 0; j < n; j++) {
                if (checkDiff(wordList.get(i), wordList.get(j))) {
                    traverseList.get(wordList.get(i)).add(wordList.get(j));
                }
            }
        }
        
        // Adding for beginWord as well
        traverseList.put(beginWord, new HashSet<String>());
        for (int i = 0; i < n; i++) {
            if (checkDiff(beginWord, wordList.get(i))) {
                traverseList.get(beginWord).add(wordList.get(i));
            }
        }
        return traverseList;
    }
}