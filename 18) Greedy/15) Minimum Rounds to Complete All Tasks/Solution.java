// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

import java.util.*;
class Solution {
    public int minimumRounds(int[] tasks) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < tasks.length; i++) {
            map.put(tasks[i], map.getOrDefault(tasks[i], 0) + 1);
        }

        int answer = 0;
        for (Integer key: map.keySet()) {
            int total = map.get(key);
            if (total == 1) return -1;

            // e.g. total tasks is 7, you can't complete two with 3. So you need to complete 1st
            // Considering 2 tasks until %3 is zero
            while (total % 3 != 0) {
                answer += 1;
                total -= 2;
            }

            // Finally complete remaining tasks in group of 3
            answer += total/3;
        }

        return answer;
    }
}