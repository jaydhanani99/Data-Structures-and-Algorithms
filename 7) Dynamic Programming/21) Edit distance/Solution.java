// A Dynamic Programming based Java program to find minimum
// number operations to convert str1 to str2
import java.io.*;

class Solution {
	static int dp[][];
	static int min(int x, int y, int z)
	{
		if (x <= y && x <= z)
			return x;
		if (y <= x && y <= z)
			return y;
		else
			return z;
	}

	static int editDistDP(String s1, String s2, int m,
						int n)
	{
		int l1 = s1.length();
		int l2 = s2.length();
		int[][] DP = new int[l1 + 1][l2 + 1];

		// initialize by the maximum edits possible
		for (int i = 0; i <= l1; i++)
			DP[i][0] = i;
		for (int j = 0; j <= l2; j++)
			DP[0][j] = j;

		// Compute the DP matrix
		for (int i = 1; i <= l1; i++) {
			for (int j = 1; j <= l2; j++) {

				// if the characters are same
				// no changes required
				if (s1.charAt(i - 1) == s2.charAt(j - 1))
					DP[i][j] = DP[i - 1][j - 1];
				else {

					// minimum of three operations possible
					DP[i][j] = min(DP[i - 1][j - 1],
								DP[i - 1][j], DP[i][j - 1])
							+ 1;
				}
			}
		}

		// initialize to global array
		dp = DP;
		for (int i = 0; i <= m; i++) {
			for (int j = 0; j <= n; j++) {
				System.out.print(dp[i][j] + ", ");
			}
			System.out.println();
		}
		return dp[m][n];
	}

	// Function to print the steps
    static void printChanges(String s1, String s2)
    {
        int i = s1.length();
        int j = s2.length();
 
        // check till the end
        while (i != 0 && j != 0) {
 
            // if characters are same
            if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                i--;
                j--;
            }
 
            // Replace
            else if (dp[i][j] == dp[i - 1][j - 1] + 1) {
                System.out.println("change " + s1.charAt(i - 1) + " to " + s2.charAt(j - 1));
                i--;
                j--;
            }
 
            // Delete the character
            else if (dp[i][j] == dp[i - 1][j] + 1) {
                System.out.println("Delete " + s1.charAt(i - 1));
                i--;
            }
 
            // Add the character
            else if (dp[i][j] == dp[i][j - 1] + 1) {
                System.out.println("Add " + s2.charAt(j - 1));
                j--;
            }
        }
		while (i > 0) {
			System.out.println("Delete " + s1.charAt(i-1));
			i -= 1;
		}
    }

	// Driver Code
	public static void main(String args[])
	{
		String str1 = "EXPONENTIAL";
		String str2 = "POLYNOMIAL";
		System.out.println(editDistDP(
			str1, str2, str1.length(), str2.length()));
		printChanges(str1, str2);
	}
}
