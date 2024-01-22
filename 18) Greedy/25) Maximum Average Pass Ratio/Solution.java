// https://leetcode.com/problems/maximum-average-pass-ratio/
// Overall idea is to increase the difference between current ratio and new ratio (by adding one student)
import java.util.*;
class StudentClass {
    public int pass, total;
    public double changeRatio;

    public StudentClass(int pass, int total, double changeRatio) {
        this.pass = pass;
        this.total = total;
        this.changeRatio = changeRatio;
    }

    public String toString() {
        return "pass = " + this.pass + " total = " + this.total + " changeRatio = " + this.changeRatio;
    }
}
class Solution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<StudentClass> pq = new PriorityQueue<>(new Comparator<StudentClass>(){
            public int compare(StudentClass s1, StudentClass s2) {
                if (s1.changeRatio < s2.changeRatio) return 1;
                else if (s1.changeRatio > s2.changeRatio) return -1;
                return 0;
            }
        });

        for (int i = 0; i < classes.length; i++) {
            StudentClass s = new StudentClass(classes[i][0], classes[i][1], (double)(classes[i][0]+1)/(double)(classes[i][1]+1) - (double)(classes[i][0])/(double)(classes[i][1]));
            pq.offer(s);
        }

        while (extraStudents > 0) {
            extraStudents--;
            StudentClass s = pq.poll();
            s.pass += 1;
            s.total += 1;
            s.changeRatio = (double)(s.pass+1)/(double)(s.total+1) - (double)(s.pass)/(double)(s.total);
            pq.offer(s);
        }

        double total = 0;
        while (pq.size() > 0) {
            StudentClass s = pq.poll();
            total += (double)(s.pass)/(double)(s.total);
        }
        return total/classes.length;
    }
}