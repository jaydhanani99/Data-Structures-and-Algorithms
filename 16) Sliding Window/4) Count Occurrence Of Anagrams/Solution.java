// https://www.youtube.com/watch?v=MW4lJ8Y0xXk&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=5&ab_channel=AdityaVerma
// Similar problem of https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        HashMap<Character, Integer> hm = new HashMap<>();
        int count = 0;
        int n = s.length();
        int m = p.length();
        
        // Creating hashmap of string s along with occurrence count
        for (int i = 0; i < m; i++) {
            Character key = p.charAt(i);
            if (hm.containsKey(key)) hm.put(key, hm.get(key)+1);
            else {
                hm.put(key, 1);
                // Increamenting count for each unique character
                count++;
            }
        }
        List<Integer> ans = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            Character key;
            key = s.charAt(i);
            // Sliding window in each iteration
            if (hm.containsKey(key)) {
                // Adding current char in our window and,
                // Decrementing occurrence count for current character of string s in hashmap
                hm.put(key, hm.get(key)-1);
                // If count is 0 that means we have current character in our window and we can decrement count as well (count of all unique chars)
                if (hm.get(key) == 0) count--;
            }
            // if count of all unique chars is zero that means we have anagram in current window and we add starting index of window in it
            if (count == 0) ans.add(i-m+1);
            

            if (i >= m - 1) {
                key = s.charAt(i-m+1);
                // Removing first element of current window and incrementing occurrence count for that element of string s in hashmap
                if (hm.containsKey(key)) {
                    // If current occurrence count is 0 that means we had this element in our window and now it is not so we have to increment count as well
                    if (hm.get(key) == 0) count++;
                    hm.put(key, hm.get(key)+1);
                }
            }
        }
        return ans;
    }
}