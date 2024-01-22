// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution {
    public boolean winnerOfGame(String colors) {
        int n = colors.length();

        if (n < 3) return false;

        int a = 1, b = 1;

        boolean turn = true; // true => alice else bob

        while (a < n && b < n) {
            // Alice
            if (turn == true) {
                // Increament alice until found the AAA
                while (a < n - 1 && (colors.charAt(a) != 'A' || colors.charAt(a-1) != 'A' || colors.charAt(a+1) != 'A')) {
                    a++;
                }

                // If reached to end of array that means no possible move
                if (a < n - 1) {
                    // Trying to find the next move in next turn
                    a++;
                } else return false;
                turn = false;
            // Bob
            } else {
                while (b < (n - 1) && (colors.charAt(b) != 'B' || colors.charAt(b-1) != 'B' || colors.charAt(b+1) != 'B')) {
                    b++;
                }

                if (b < (n-1)) {
                    b++;
                } else return true;
                turn = true;
            }
        }
        return false;
    }
}