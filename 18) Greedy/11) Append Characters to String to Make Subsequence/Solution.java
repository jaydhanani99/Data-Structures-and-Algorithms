
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution {
    public int appendCharacters(String s, String t) {
        int i = 0, j = 0, n = s.length(), m = t.length();
        while (i < n && j < m) {
            // If char is mathced increase the both the pointer else only increase pointer of string s so we can have further look for string match
            if (s.charAt(i) == t.charAt(j)) {
                j++;
            }
            i++;        
        }

        return j < m ? (m-j) : 0;
    }
}