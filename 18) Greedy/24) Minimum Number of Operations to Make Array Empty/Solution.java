// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

import java.util.*;
class Solution {
    public int minOperations(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        int answer = 0;

        for (Integer key: map.keySet()) {
            int current = map.get(key);
            if (current == 1) return -1;

            answer += (current/3) + (current % 3 != 0 ? 1 : 0);

            // Alternatively
            // if (current % 3 == 0) answer += current/3;
            // else {
            //     while (current % 3 != 0) {
            //         current -= 2;
            //         answer++;
            //     }

            //     answer += current/3;
            // }
        }

        return answer;
    }
}