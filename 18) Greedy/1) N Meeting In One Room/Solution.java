// https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
import java.util.*;
class Item {
    public int start, end;
    public Item(int start, int end) {
        this.start = start;
        this.end = end;
    }
}
class Solution 
{
    //Function to find the maximum number of meetings that can
    //be performed in a meeting room.
    public static int maxMeetings(int start[], int end[], int n)
    {
        ArrayList<Item> a = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            a.add(new Item(start[i], end[i]));
        }
        
        Collections.sort(a, new Comparator<Item>() {
           public int compare (Item i1, Item i2) {
               if (i1.end < i2.end) return -1;
               else if (i1.end > i2.end) return 1;
               return 0;
           } 
        });
        
        int answer = 0;
        int previousFinish = -1;
        for (int i = 0; i < n; i++) {
            if (previousFinish < a.get(i).start) {
                answer++;
                previousFinish = a.get(i).end;
            }
        }
        return answer;
    }
}