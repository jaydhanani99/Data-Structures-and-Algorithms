// https://leetcode.com/problems/4sum-ii/

class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                int sum = nums1[i]+nums2[j];
                if (map.containsKey(sum)) map.put(sum, map.get(sum)+1);
                else map.put(sum, 1);
            }
        }
        for (int i = 0; i < nums3.length; i++) {
            for(int j = 0; j < nums4.length; j++) {
                if (map.containsKey(-(nums3[i]+nums4[j]))) answer+=map.get(-(nums3[i]+nums4[j]));
            }
        }
        return answer;
    }
}