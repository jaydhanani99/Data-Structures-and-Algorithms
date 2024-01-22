import java.util.*;

class Solution {
    public List<Integer> partitionLabels(String s) {
        char[] c = s.toCharArray();
        int n = c.length;

        HashMap<Character, Integer> h = new HashMap<>();

        for (int i = 0; i < n; i++) {
            h.put(c[i], i);
        }

        int maxIndex = 0;
        int currentCount = 0;
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            maxIndex = Math.max(maxIndex, h.get(c[i])); // This would essentially gives the maximum index of ending chars of current window
            currentCount++;
            // When we reach the end of current window that means we convered all the chars for current window
            if (i == maxIndex) {
                answer.add(currentCount);
                currentCount = 0;
            }
        }
        return answer;
    }
    // public List<Integer> partitionLabels(String s) {
    //     char[] c = s.toCharArray();
    //     int n = c.length;

    //     HashMap<Character, Integer> h = new HashMap<>();

    //     for (int i = 0; i < n; i++) {
    //         h.put(c[i], h.getOrDefault(c[i], 0) + 1);
    //     }

    //     HashMap<Character, Integer> current = new HashMap<>();
    //     int currentCount = 0;
    //     List<Integer> answer = new ArrayList<>();

    //     for (int i = 0; i < n; i++) {
    //         current.put(c[i], current.getOrDefault(c[i], 0) + 1);
    //         currentCount++;

    //         if (current.getOrDefault(c[i], 0) == h.getOrDefault(c[i], 0)) {
    //             current.remove(c[i]);
    //         }

    //         if (current.size() == 0) {
    //             answer.add(currentCount);
    //             currentCount = 0;
    //         }
    //     }

    //     return answer;
    // }
}