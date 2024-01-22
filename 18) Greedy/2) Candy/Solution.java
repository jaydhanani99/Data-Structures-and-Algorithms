// https://leetcode.com/problems/candy/

class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;

        if (n == 1) return 1;

        int[] candies = new int[n];
        for (int i = 0; i < n; i++) {
            candies[i] = 1;
        }

        // Adding candies+1 of previous student if current student has greater rating than the previous one
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) candies[i] = candies[i-1] + 1;
        }

        int answer = candies[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            // Only adding candies+1 if current rating is greater than next and current candy is less than or equal to next
            if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i+1]) candies[i] = candies[i+1] + 1;
            answer += candies[i];
        }

        return answer;
        
    }
}