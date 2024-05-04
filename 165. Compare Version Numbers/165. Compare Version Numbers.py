class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n1 = len(v1)
        n2 = len(v2)
        
        for i in range(max(n1,n2)):
            left = int(v1[i]) if i<n1 else 0
            right = int(v2[i]) if i<n2 else 0
            if left > right :
                return 1
            elif right > left :
                return -1

        return 0
        