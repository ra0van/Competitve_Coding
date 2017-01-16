#https://leetcode.com/contest/leetcode-weekly-contest-15/problems/max-consecutive-ones/
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        count=0
        for i in nums:
            if i==1:
                count+=1
                if count>max_count:
                    max_count=count
            else:
                count=0
        return int(max_count)
            
        
