# 49. Group Anagrams

## Intuition
The intuition behind this problem is that anagrams will have the same sorted characters, so we can use this property to group anagrams together.

## Approach
The approach involves iterating through each word in the input list of strings. For each word, we sort its characters and use the sorted string as a key in a dictionary. If the sorted string already exists in the dictionary, we append the word to the corresponding list. Otherwise, we create a new entry in the dictionary with the sorted string as the key and a list containing the word as the value. Finally, we return the values of the dictionary as the grouped anagrams.

## Complexity
- Time complexity:
  - Sorting each word takes O(k * logk) time, where k is the length of the longest word in the input list.
  - We iterate through each word in the input list, so the overall time complexity is O(n * klogk), where n is the number of words in the list.
- Space complexity:
  - We use a dictionary to store the grouped anagrams, which can have a maximum of n entries.
  - Each entry in the dictionary contains a list of words.
  - Therefore, the space complexity is O(n * m), where m is the average length of words in the input list.

## Code
``` python 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            sword = ''.join(sorted(word))
            if sword in ans:
                ans[sword].append(word)
            else :
                ans[sword] = [word]

        return list(ans.values())
        
```