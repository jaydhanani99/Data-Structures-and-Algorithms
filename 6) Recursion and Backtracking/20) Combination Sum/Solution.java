// https://leetcode.com/problems/combination-sum/

import java.util.*;
class Solution {
    public static List<List<Integer>> answer;

    public Solution() {
        answer = new ArrayList<>();
    }

    private void traverse(List<Integer> current, int i, int[] candidates, int target) {
        if (i >= candidates.length) return;
        if (target < 0) return;
        if (target == 0) {
            answer.add(new ArrayList<>(current));
            return;
        }

        // Three options
        // 1) Do not include current element
        traverse(current, i + 1, candidates, target);
        // 2) include current element and reconsider current element
        current.add(candidates[i]);
        traverse(current, i, candidates, target - candidates[i]);
        current.remove(current.size() - 1); // Removing element so we don't need to create copy of list
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // Arrays.sort(candidates);
    
        traverse(new ArrayList<>(), 0, candidates, target);
        return answer;

    }
}