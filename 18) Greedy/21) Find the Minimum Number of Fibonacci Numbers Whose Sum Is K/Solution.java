// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

import java.util.*;
class Solution {
    public int findMinFibonacciNumbers(int k) {
        // Generating fib numbers till we get last greater than k
        List<Integer> fib = new ArrayList<>();

        int fib1 = 1;
        int fib2 = 1;
        fib.add(1);
        fib.add(1);
        while (fib2 < k) {
            int current = fib1 + fib2;
            fib.add(current);
            fib1 = fib2;
            fib2 = current;
        }

        int n = fib.size() - 1;
        int answer = 0;
        while (k > 0) {
            if (fib.get(n) <= k) {
                k -= fib.get(n);
                answer++;
            }
            n--;
        }

        return answer;
    }

    // public int findMinFibonacciNumbers(int k) {
    //     if (k <= 3) return 1;
    //    // Generating fib numbers till we get last greater than k
    //     int[] fib = new int[45]; // Since 45th fib number is greater than maximum value of k 10^9
    //     fib[0] = 1;
    //     fib[1] = 1;
    //     int n = 1;
    //     while (k >= fib[n]) {
    //         int current = fib[n-1] + fib[n];
    //         fib[++n] = current;
    //     }

    //     int answer = 0;
    //     while (k > 0) {
    //         if (fib[n] <= k) {
    //             k -= fib[n];
    //             answer++;
    //         }
    //         n--;
    //     }

    //     return answer;
    // }
}