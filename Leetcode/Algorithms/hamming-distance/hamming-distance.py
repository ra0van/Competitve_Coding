#https://leetcode.com/problems/hamming-distance/
class Solution(object):
    def hammingDistance(self, x, y):
        a,b = x,y
        
        binA = self.getBinaryString(a)
        binB = self.getBinaryString(b)
        lA = len(binA)
        lB = len(binB)
        if lA>lB:
        	binB = ('0'*(lA-lB)) + binB
        	
        elif lB>lA:
        	binA = ('0'*(lB-lA)) + binA
        	
        
        count = 0
        for i in xrange(max(lB,lA)):
        	if binA[i]!=binB[i]:
        		count +=1
        
        return count
        
    def getBinaryString(self,n):
    	bit = ''
    	while n!=0:
    		rem = n%2
    		n = n/2
    		bit = str(rem)+bit
    	return bit

