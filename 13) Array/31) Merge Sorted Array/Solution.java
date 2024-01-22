// https://leetcode.com/problems/merge-sorted-array/

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        // To fill the final nums array from last
        int finalPointer = nums1.length - 1;

        while (i >= 0 && j >= 0) {
            if (nums1[i] >= nums2[j]) {
                nums1[finalPointer] = nums1[i];
                i--;
            } else {
                nums1[finalPointer] = nums2[j];
                j--;
            }
            finalPointer--;
        }

        while (i >= 0) {
            nums1[finalPointer] = nums1[i];
            i--;
            finalPointer--;
        }

        while (j >= 0) {
            nums1[finalPointer] = nums2[j];
            j--;
            finalPointer--;
        }
    }
}