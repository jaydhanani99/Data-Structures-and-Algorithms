// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int maxElementFromLast[] = new int[n];

        int max = Integer.MIN_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            max = Math.max(max, prices[i]);
            maxElementFromLast[i] = max;
        }

        int answer = Integer.MIN_VALUE;
        for (int i = 0; i < prices.length; i++) {
            answer = Math.max(answer, maxElementFromLast[i] - prices[i]);
        }
        return answer;
    }
}