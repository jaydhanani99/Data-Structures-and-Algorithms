# https://www.youtube.com/watch?v=l45md3RYX7c&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=12

class Solution:
    def towerOfHanoi(self, n, source_rod, helper_rod, destination_rod):
        if n == 1:
            # If only 1 disk in initial rod(from_rod)
            print('Move disk from', source_rod, 'to', destination_rod)
            return
        
        # we move n-1 disks from source_rod to helper_rod using destination_rod
        self.towerOfHanoi(n-1, source_rod, destination_rod, helper_rod)
        # now we move nth disk to destination_rod
        print('Move disk from', source_rod, 'to', destination_rod)
        # After moving nth disk, we move all the disk from helper_node to destination_rod using source_rod
        self.towerOfHanoi(n-1, helper_rod, source_rod, destination_rod)

    def solve(self, n):
                        # n, source, helper, destination
        self.towerOfHanoi(n, 'A', 'B', 'C')

sol = Solution()
sol.solve(15)