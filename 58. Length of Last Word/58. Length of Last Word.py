class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = 0
        count = 0
        s = ' ' + s
        i = len(s)-1


        while i>0:
            if s[i] != ' ':
                word = 1
            if word :
                if s[i] == ' ':
                    break
                count+=1
            i-=1

        return count
        