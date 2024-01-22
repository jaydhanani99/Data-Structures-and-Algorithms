// https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

import java.util.*;

class Job {
    int id, profit, deadline;
    Job(int x, int y, int z){
        this.id = x;
        this.deadline = y;
        this.profit = z; 
    }
}

class Solution
{
    //Function to find the maximum profit and the number of jobs done.
    int[] JobScheduling(Job arr[], int n)
    {
        // Your code here
        Arrays.sort(arr, new Comparator<Job>() {
           public int compare(Job j1, Job j2) {
               if (j1.profit > j2.profit) return -1;
               else if (j1.profit < j2.profit) return 1;
               return 0;
           } 
        });
        
        int maxDeadline = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            maxDeadline = Math.max(maxDeadline, arr[i].deadline);
        }
        
        int deadline[] = new int[maxDeadline+1];
        int answer = 0;
        int total = 0;
        
        for (int i = 0; i < n; i++) {
            // Always better to do the job on it's deadline. 
            // If at that deadline already another job is done then decrease the deadline until found the empty slot
            for (int j = arr[i].deadline; j > 0; j--) {
                if (deadline[j] == 0) {
                    deadline[j] = i+1; // Storing i+1 because i starts from 0 and we're checking deadline[j] == 0
                    answer += arr[i].profit;
                    total++;
                    break;
                }
            }
        }
        
        return new int[]{total, answer};
    }
}