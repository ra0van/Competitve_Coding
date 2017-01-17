#https://leetcode.com/problems/hamming-distance/
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''

class Solution(object):
    
    '''
        My first solution.
        
    '''
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
       
    '''
        Can use python inbuilt bin() method instead, which returns  '0bxxxxx'.
    '''
    def getBinaryString(self,n):
    	bit = ''
    	while n!=0:
    		rem = n%2
    		n = n/2
    		bit = str(rem)+bit
    	return bit
    
    '''
        Another solution 
    '''
    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        while x or y:
            count += (x%2)^(y%2)
            x/=2
            y/=2
        return count

