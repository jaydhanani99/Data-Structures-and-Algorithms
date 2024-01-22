# https://www.interviewbit.com/old/problems/2-sum/

class Solution:
	# @param numbers : tuple of integers
	# @param target : integer
	# @return a list of integers
	def twoSum(self, nums, target):
        n = len(nums)
        dict = {}
        ans = []
        for i in range(n):
            # First check that target-nums[i] exists in dict or not
            if (target-nums[i]) in dict:
                # If we have not encountered ans so far add this solution in ans
                if not ans:
                    ans = [dict[target-nums[i]], i+1]
                else:
                    # if we have found the ans and index2 is greater than the current index 2 replace the answer
                    # or index2 is same as current index2 and index1 is greater than the current index1 replace the answer
                    if ans[1] > i+1 or (ans[1] == i+1 and ans[0] > dict[target-nums[i]]):
                        ans = [dict[target-nums[i]], i+1]
            
            # We would add in dict only if not exists, so that we have minimum index in dict
            if nums[i] not in dict:
                # Adding current element in dict
                dict[nums[i]] = i+1
        return ans