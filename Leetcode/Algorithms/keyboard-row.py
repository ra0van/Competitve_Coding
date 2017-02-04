class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        l=[]
        for word in words:
            orgWord = word
            word = word.lower()
            if word[0] in row1:
                row = row1
            elif word[0] in row2:
                row = row2
            elif word[0] in row3:
                row = row3
            else:
                continue
            isTrue = True
            for w in word:
                if w not in row:
                    isTrue = False
                    break
            if isTrue:
                l.append(orgWord)
        return l
                
            
