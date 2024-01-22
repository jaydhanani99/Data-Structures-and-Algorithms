// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/description/
import java.util.*;
class Solution {
    // Optimized approach
    public int numOfPairs(String[] nums, String target) {
        // This is just a two sum problem if we consider string length to int
        HashMap<String, Integer> h = new HashMap<>();
        int answer = 0;

        for (int i = 0; i < nums.length; i++) {
            h.put(nums[i], h.getOrDefault(nums[i], 0) + 1);
        }

        for (int i = 0; i < nums.length; i++) {
            // We are just making sure that current nums is equal to prefix of target and finding rest of target string in hashmap
            // e.g. nums[i] = 43403 and target is 434034, then we just add total number of "4" available in map
            if (target.indexOf(nums[i]) == 0) {
                String key = target.substring(nums[i].length());
                if (h.containsKey(key)) {
                    answer += h.get(key);
                    if (key.equals(nums[i])) answer -= 1;
                }
            }
        }
        return answer;
    }

    // Naive approach
    // public int numOfPairs(String[] nums, String target) {
    //     int answer = 0;
    //     for (int i = 0; i < nums.length; i++) {
    //         for (int j = 0; j < nums.length; j++) {
    //             if (i == j) continue;
    //             if ((nums[i] + nums[j]).equals(target)) answer++;
    //         }
    //     }
    //     return answer;
    // }
}