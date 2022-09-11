import java.util.Stack;

// # https://practice.geeksforgeeks.org/problems/sort-a-stack/1

// # Same as sort array using recursion

class Solution{
    public void insert(Stack<Integer> s, int element) {
        if (s.size() == 0 || s.peek() <= element) {
            s.push(element);
            return;
        }
        int current_element = s.pop();
        insert(s, element);
        s.push(current_element);
    }
    
	public Stack<Integer> sort(Stack<Integer> s)
	{
		//add code here.
		if (s.size() == 1) return s;
		int element = s.pop();
		sort(s);
		insert(s, element);
		return s;
	}
}