#https://leetcode.com/problems/max-consecutive-ones-ii
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        import sys
        #nums = map(int,raw_input().split())
        
        l = len(nums)
        prev = nums[0]
        count = 1
        i =1  
        bitA = []
        bitC = []
        min_zero_gap = sys.maxsize
        while (i<l):
            curr = nums[i]
            if prev==curr:
                count+=1
            else:
                if prev==0:
                    if count<min_zero_gap:
                        min_zero_gap = count
                bitA.append(prev)
                bitC.append(count)
                prev = curr
                count = 1
            i+=1
        if prev==0:
            if count<min_zero_gap:
                min_zero_gap = count
        bitA.append(prev)
        bitC.append(count)
        count=0
        max_count=0
        if min_zero_gap>1 and len(bitA)!=1:
            return max(bitC)+1
        elif len(bitA)==1 and bitA[0]==1:
            return bitC[0]
        elif len(bitA)==1 and bitA[0]==0:
            return 1
        else:
            sum_arr = []
            zero_ind = 0
            if bitA[0]==1:
                zero_ind = 1
            l = len(bitA)
            while zero_ind<l:
                s = 1
                if bitA[zero_ind]==0 and bitC[zero_ind]==1 :
                    if zero_ind-1>=0:
                        s += (bitC[zero_ind-1])
                    if zero_ind+1<l:
                        s += (bitC[zero_ind+1])
                    sum_arr.append(s)
                elif bitA[zero_ind]==0 and bitC[zero_ind]>1:
                    s1=0
                    if zero_ind-1>=0:
                        s = (bitC[zero_ind-1]+1)
                    if zero_ind+1<l:
                        s1 = (bitC[zero_ind+1]+1)
                    # print s,s1
                    sum_arr.append(max(s,s1))
                zero_ind+=1
            return max(sum_arr)
                    
        
        

        
        
        
