class Solution:
    def checkValidString(self, s: str) -> bool:
        mins, maxs = 0, 0

        for c in s:
            if c == "(":
                mins, maxs = mins + 1, maxs + 1
            elif c == ")":
                mins, maxs = mins - 1, maxs - 1
            else:
                mins, maxs = mins - 1, maxs + 1
            if maxs < 0:
                return False
            if mins < 0:
                mins = 0
        return mins == 0
        