// https://www.hackerrank.com/challenges/friend-circle-queries/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the maxCircle function below.
    static HashMap<Integer, Integer> parent;
    static HashMap<Integer, Integer> count;
    static int max;
    static void union(HashMap<Integer, Integer> parent, int x, int y) {
        if (!parent.containsKey(x)) {
            parent.put(x, x);
            count.put(x, 1);
        }
        
        if (!parent.containsKey(y)) {
            parent.put(y, y);
            count.put(y, 1);
        }
        
        int p1 = find(x);
        int p2 = find(y);
        // If they both belongs to same group no need to do anything
        if (p1 == p2) return;
        int s1 = count.get(p1);
        int s2 = count.get(p2);
        
        // then we will make parent of p2 as p1
        if (s1 > s2) {
            parent.put(p2, p1);
            count.put(p1, s1+s2);
        } else {
            parent.put(p1, p2);
            count.put(p2, s1+s2);
        }
        if (s1 + s2 > max) max = s1 + s2;
    }
    
    static int find(int x) {
        if (parent.get(x) == x) return x;
        return find(parent.get(x));
    }
    static int[] maxCircle(int[][] queries) {
        parent = new HashMap<>();
        count = new HashMap<>();
        max = 0;

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            union(parent, queries[i][0], queries[i][1]);
            ans[i] = max;
        }
        
        System.out.println(count);
        return ans;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[][] queries = new int[q][2];

        for (int i = 0; i < q; i++) {
            String[] queriesRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 2; j++) {
                int queriesItem = Integer.parseInt(queriesRowItems[j]);
                queries[i][j] = queriesItem;
            }
        }

        int[] ans = maxCircle(queries);

        for (int i = 0; i < ans.length; i++) {
            bufferedWriter.write(String.valueOf(ans[i]));

            if (i != ans.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
