# https://practice.geeksforgeeks.org/problems/game-of-death-in-a-circle1840/1#
# https://www.youtube.com/watch?v=ULUNeD0N9yI&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=19

class Solution:
    def solve(self, people, k, current_index):
        n = len(people)
        if n == 1:
            return people[0]
            
        # Finding next index to eliminate person    
        current_index = ((current_index+k)%n)
        
        # Removing current person
        people.pop(current_index)
        return self.solve(people, k, current_index)
                
        
        
    def safePos(self, n, k):
        # With Recursion (In some sites you will get maximum recursion depth exceed)
        # As we are considering current index as next index
        k = k - 1
        return self.solve([i for i in range(1, n+1)], k, 0)
        
        
        # Without recursion
        index   = 0
        arr     = [i for i in range(1, n+1)]
        k       = k - 1
        arr_length = n
        while arr_length > 1:
            index = ((index+k)%arr_length)
            arr.pop(index)
            arr_length -= 1
        return arr[0]
            