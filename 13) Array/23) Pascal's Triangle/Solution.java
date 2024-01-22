// https://leetcode.com/problems/pascals-triangle/
import java.util.*;
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> output = new ArrayList<>();
        output.add(new ArrayList<>(Arrays.asList(1)));
        
        if (numRows == 1) return output;
        
        output.add(new ArrayList<>(Arrays.asList(1,1)));
        if (numRows == 2) return output;
        
        for (int i = 2; i < numRows; i++) {
            List<Integer> current = new ArrayList<>();
            List<Integer> previous = output.get(i-1);
            current.add(1);
            
            int n = previous.size();
            
            for (int j = 1; j < n; j++) {
                current.add(previous.get(j)+previous.get(j-1));
            }
            current.add(1);
            output.add(current);
        }
        return output;
    }
}