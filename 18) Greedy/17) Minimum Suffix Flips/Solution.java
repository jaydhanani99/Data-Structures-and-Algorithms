// https://leetcode.com/problems/minimum-suffix-flips/


class Solution {
    public int minFlips(String target) {
        // We just need to return the total number of chaning bits
        // However one less flip is require if first char is 0 as final string contains all the 0 so no flip is needed for first zeros.
        int answer = 0;
        char previous = '0'; // Considering previous as 0 which would count one less flip if first char of target is 0
        for (char ch: target.toCharArray()) {
            if (previous != ch) {
                answer++;
            }
            previous = ch;
        }

        return answer;
    }
}