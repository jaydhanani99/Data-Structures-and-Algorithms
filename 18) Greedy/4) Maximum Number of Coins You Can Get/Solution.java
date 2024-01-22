// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

import java.util.*;

class Solution {
    public int maxCoins(int[] piles) {
        int answer = 0;
        Arrays.sort(piles);

        int i = piles.length - 2;
        int count = piles.length/3;
        while (count > 0) {
            answer += piles[i];
            count--;
            i -= 2;
        }
        return answer;
    }
}