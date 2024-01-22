// https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution {
    public long[] sumOfThree(long num) {
        if (num % 3 != 0) return new long[0];

        num = num/3;
        return new long[] { num - 1, num, num + 1 };
    }
}