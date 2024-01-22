// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

import java.util.*;
class Item {
    public int plantTime, growTime;

    public Item(int plantTime, int growTime) {
        this.plantTime = plantTime;
        this.growTime = growTime;
    }
}

class Solution {
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        int n = plantTime.length;
        Item[] time = new Item[n];

        for (int i = 0; i < n; i++) {
            time[i] = new Item(plantTime[i], growTime[i]);
        }

        /*
         The only concern is when the last seed will blow right?
         So our final answer is depend on the blow of last seed.
         Somehow we need to minimize it and the only way we can do that is having a seed that have lowest blow time in last.
         Anyway we are planting any seed in sequential manner and it won't affect answer if you plant one seed half and second seed and again one seed. This would not improve the answer. Because at the end you won't have any empty day without planting.
         So best choice is first plant seed which have larger blow time. Since blow time is not affecting the plant time and we
            only have restriction with plant time.
         */


        // Sorting by grow time in descending order
        Arrays.sort(time, new Comparator<Item>() {
            public int compare(Item i1, Item i2) {
                if (i1.growTime > i2.growTime) return -1;
                else if (i1.growTime < i2.growTime) return 1;
                return 0;
            }
        });

        int answer = 0;
        int currentDay = -1;
        for (int i = 0; i < n; i++) {
            currentDay += time[i].plantTime;
            answer = Math.max(answer, currentDay + time[i].growTime + 1);
        }
        return answer;
    }
}