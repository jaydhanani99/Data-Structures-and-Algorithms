// https://leetcode.com/problems/optimal-partition-of-string/

import java.util.*;
class Solution {
    public int partitionString(String s) {
        HashSet<Character> current = new HashSet<>();
        int answer = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            if (current.contains(s.charAt(i))) {
                answer++;
                current = new HashSet<>();
            }
            current.add(s.charAt(i));
        }

        return answer+1;
    }
}