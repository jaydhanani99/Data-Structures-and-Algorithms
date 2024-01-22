// https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
// https://practice.geeksforgeeks.org/problems/union-find/0/

public class Solution
{
    // To get actual paent of a
    int find(int par[], int a) {
        if (par[a] == a) return a;
        // Doing path compression by making par[a] = find(par, par[a])
        return par[a] = find(par, par[a]);
    }

    //Function to merge two nodes a and b.
    void union_( int a, int b, int par[], int rank[]) 
    {
        //code here
        // We do union using rank
        // First we get parent of a and b
        int aParent = find(par, a);
        int bParent = find(par, b);
        
        if (rank[aParent] > rank[bParent]) {
            // This condition means that aParent has larger chlidren compare to bParent
            // So we will not make child of bParent to aParent as this would cause increase in rank for bParent
            // So we will make child of aParent to bParent (or parent of bParent to aParent)
            par[bParent] = aParent;
        }else if (rank[aParent] < rank[bParent]) {
            par[aParent] = bParent;
        }else{
            // If both have same rank we can make anyone to parent
            // Here we have made aParent -> bParent, so we have increased rank of aParent
            par[bParent] = aParent;
            rank[aParent] += 1;
        }
    }
    
    //Function to check whether 2 nodes are connected or not.
    bool isConnected(int x,int y, int par[], int rank[])
    {
        //code here
        if (find(par, x) == find(par, y)) return true;
        return false;
    }
};