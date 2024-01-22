// https://leetcode.com/problems/reducing-dishes/

import java.util.*;
class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        int n = satisfaction.length;

        if (n == 0) return 0;

        Arrays.sort(satisfaction);


        // After sorting finding the sum of elements from last until it's < 0
        // When the sum is < 0 at that moment our overall answer would be less
        // When the sum is >= 0 at that moment our overall answer would be maximum
        int currentSum = 0, i = n - 1;
        for (; i >= 0; i--) {
            currentSum += satisfaction[i];
            if (currentSum < 0) {
                i++;
                break;
            }
        }

        // In case sum of all the elements is > 0
        if (i < 0) i = 0;

        // After finding the starting index, we'll do the sum of like-time coefficient from that index
        int coefficient = 1;
        int answer = 0;
        while (i < n) {
            answer += (coefficient * satisfaction[i]);
            coefficient++;
            i++;
        }
        return answer;
    }
}