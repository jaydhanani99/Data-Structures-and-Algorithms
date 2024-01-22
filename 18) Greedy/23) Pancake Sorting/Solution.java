// https://leetcode.com/problems/pancake-sorting/

import java.util.*;
class Solution {
    public void flip(int[] arr, int end) {
        int start = 0;
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
    public List<Integer> pancakeSort(int[] arr) {
        // Step 1: Idea is to start from last index e.g. start with 4 for input [3, 2, 4, 1] and find the index
        // Step 2: Reverse from start index 0 to end index of that element (2 in our case)
        // So our array would be ([4, 2, 3, 1])
        // Step 3: Now reverse array starting from 0 to current element -1 (0 to 3) so our array would be [1, 3, 2, 4]
        // Step 4: Now decreament the last index and repeat this process
        // In case of end index is already current index, we'll skip step 2 and 3.
        // In case of end index is already at 0, we'll skip Step 2
        
        int currentLastElement = arr.length;
        List<Integer> output = new ArrayList<>();

        while (currentLastElement > 1) {
            for (int i = 0; i < arr.length; i++) {
                int currentLastElementIndex = currentLastElement - 1;
                if (arr[i] == currentLastElement) {
                    if (i == currentLastElementIndex) { // max element at already last location 
                        currentLastElement--;
                        break;
                    }

                    if (i != 0) {
                        output.add(i+1);
                        flip(arr, i);
                    }
                    output.add(currentLastElement);
                    flip(arr, currentLastElementIndex);
                    currentLastElement--;
                    break;
                }
            }
        }
        return output;
    }
}