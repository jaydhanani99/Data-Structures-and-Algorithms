// https://leetcode.com/problems/reduce-array-size-to-the-half/

import java.util.*;
class Solution {
    public int minSetSize(int[] arr) {
        HashMap<Integer, Integer> h = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            h.put(arr[i], h.getOrDefault(arr[i], 0) + 1);
        }

        if (arr.length == h.size()) return arr.length/2;

        ArrayList<Integer> a = new ArrayList<>();
        for (Integer key: h.keySet()) {
            a.add(h.get(key));
        }

        Collections.sort(a, Comparator.reverseOrder());

        int answer = 0;
        int total = 0;
        for (int i = 0; i < a.size(); i++) {
            total += a.get(i);
            answer++;
            if (total >= arr.length/2) return answer;
        }
        return answer;
    }
}