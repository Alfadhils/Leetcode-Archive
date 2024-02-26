class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        p = ''
        if s[0] == '-':
            s = s[1:]
            p = '-'
        elif s[0] == '+':
            s = s[1:]
        
        res = ''
        for i in s:
            if i.isdigit():
                res += i
            else :
                break
        
        if not res:
            res += '0'
        else :
            res = p + res

        return min(max(int(res), -2**31), 2**31 - 1)
        