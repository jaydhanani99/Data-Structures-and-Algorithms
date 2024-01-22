// https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

import java.util.*;

class Item {
    int value, weight;
    Item(int x, int y){
        this.value = x;
        this.weight = y;
    }
}
class Solution
{
    //Function to get the maximum total value in the knapsack.
    double fractionalKnapsack(int W, Item arr[], int n) 
    {
        Arrays.sort(arr, new Comparator<Item>() {
            public int compare(Item i1, Item i2) {
                if (((double)i1.value/(double)i1.weight) > ((double)i2.value/(double)i2.weight)) return -1;
                else if (((double)i1.value/(double)i1.weight) < ((double)i2.value/(double)i2.weight)) return 1;
                return 0;
            }
        });
        
        int i = 0;
        double answer = 0;
        while (i < n && W > 0) {
            if (arr[i].weight <= W) {
                W -= arr[i].weight;
                answer += arr[i].value;
            } else {
                answer += (double)(W*arr[i].value)/(double)arr[i].weight;
                break; // W = 0
            }
            i++;
        }
        
        return answer;
    }
}