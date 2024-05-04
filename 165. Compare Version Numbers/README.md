# 165. Compare Version Numbers

## Intuition
The problem involves comparing two version numbers represented as strings. We need to return an integer indicating whether version1 is greater than, equal to, or less than version2. My initial thought is to split the versions by the '.' delimiter and then iterate through each component to compare them.

## Approach
I split both version strings into lists of their components using the '.' delimiter. Then, I find the maximum length between the two lists to ensure proper iteration. I iterate through the lists and compare each component at the same index. If one list ends before the other, I consider the remaining components as zeros. During comparison, if a component from version1 is greater than the corresponding component from version2, I return 1 indicating version1 is greater. If the opposite is true, I return -1. If all corresponding components are equal, I return 0.

## Complexity
- Time complexity: 
  - The time complexity of splitting the strings into lists is O(n), where n is the length of the longer version string.
  - The time complexity of the iteration is O(max(n1, n2)), where n1 and n2 are the lengths of the version lists.
  - Overall time complexity is O(n).
  
- Space complexity:
  - The space complexity is O(n1 + n2), where n1 and n2 are the lengths of the version lists. This is due to the storage of the split version components in the lists v1 and v2.

## Code
```python
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
```