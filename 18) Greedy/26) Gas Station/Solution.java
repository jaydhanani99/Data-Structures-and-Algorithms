// https://leetcode.com/problems/gas-station/

class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int answer = 0;
        int currentRemainingGas = 0;
        int totalRemainingGas = 0;
        for (int i = 0; i < gas.length; i++) {
            currentRemainingGas += gas[i] - cost[i];
            totalRemainingGas += gas[i] - cost[i];
            if (currentRemainingGas < 0) {
                currentRemainingGas = 0;
                answer = i+1;
            }
        }
        return totalRemainingGas >= 0 ? answer : -1;
    }
}