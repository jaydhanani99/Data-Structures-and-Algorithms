// https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
import java.util.Arrays;
class Solution {
    public void reverse(int[] nums) {
        reverse(nums, 0);
    }

    public void reverse(int[] nums, int i) {
        int j = nums.length - 1;
        while (i < j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        // Find the element which is less than the previous element from last
        int index = -1;
        for (int i = n - 1; i > 0; i--) {
            if (nums[i-1] < nums[i]) {
                index = i - 1;
                break;
            }
        }
        if (index == -1) {
            reverse(nums);
        } else {
            // Find the next greater element of i (it can directly be found by finding first max from right)
            for (int i = n - 1; i > index; i--) {
                if (nums[i] > nums[index]) {
                    int temp = nums[i];
                    nums[i] = nums[index];
                    nums[index] = temp;
                    break;
                }
            }

            // Reverse the right half
            reverse(nums, index+1);
        }
    }
}