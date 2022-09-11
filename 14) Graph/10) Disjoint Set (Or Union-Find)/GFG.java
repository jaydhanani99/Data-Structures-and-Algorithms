// https://practice.geeksforgeeks.org/problems/disjoint-set-union-find/1
class GfG
{
	int find(int A[],int X)
    {
        //add code here.
        if (A[X] == X) return X;
        return find(A, A[X]);
	}
	void unionSet(int A[],int X,int Z)
    {
        //add code here.
        int XParent = find(A, X);
	    int ZParent = find(A, Z);
	    A[XParent] = ZParent;
	}
}