import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// https://leetcode.com/problems/4sum/
// https://www.interviewbit.com/problems/4-sum/

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        int n = nums.length;
        List<List<Integer>> answer = new ArrayList<>();
        
        for (int i = 0; i < n-1; i++) {
            for (int j = i + 1; j < n-2; j++) {
                int start = j+1;
                int end = n-1;
                while (start < end) {
                    // System.out.println("i"+nums[i]+"j"+nums[j]+"start"+nums[start]+"end"+nums[end]);
                    int currentSum = nums[i]+nums[j]+nums[start]+nums[end];
                    if (currentSum == target) {
                        List<Integer> currentAnswer = new ArrayList<>();
                        currentAnswer.add(nums[i]);
                        currentAnswer.add(nums[j]);
                        currentAnswer.add(nums[start]);
                        currentAnswer.add(nums[end]);
                        answer.add(currentAnswer);
                        // After considering this start and end, skipping the same elements
                        while (start < end && nums[start] == nums[start+1]) start++;
                        start++;
                        while (start < end && nums[end] == nums[end-1]) end--;
                        end--;
                    }else if (currentSum < target) start++;
                    else end--;
                }
                // skipping the same elements
                while (j < n-2 && nums[j] == nums[j+1]) j++;
            }
            // skipping the same elements
            while (i < n-1 && nums[i] == nums[i+1]) i++;
        }
        return answer;
    }
}