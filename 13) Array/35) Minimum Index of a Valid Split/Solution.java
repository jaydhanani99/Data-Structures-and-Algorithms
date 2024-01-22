// https://leetcode.com/problems/minimum-index-of-a-valid-split/

import java.util.*;
class Solution {
    public int minimumIndex(List<Integer> nums) {
        HashMap<Integer, Integer> right = new HashMap<>();
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            right.put(nums.get(i), right.getOrDefault(nums.get(i), 0) + 1);
        }

        HashMap<Integer, Integer> left = new HashMap<>();

        for (int i = 0; i < n; i++) {
            left.put(nums.get(i), left.getOrDefault(nums.get(i), 0) + 1);
            right.put(nums.get(i), right.get(nums.get(i)) - 1);

            boolean leftDominant = left.get(nums.get(i)) * 2 > (i + 1);
            boolean rightDominant = right.get(nums.get(i)) * 2 > (n - i - 1);
            if (leftDominant == true && rightDominant == true) return i;
        }
        return -1;
    }
}