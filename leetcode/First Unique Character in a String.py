class Solution:
    def firstUniqChar(self, s: str) -> int:
        d =  {i:s.count(i) for i in s}
        for i, j in d.items():
            if j == 1:
                for x in range(len(s)):
                    if i == s[x]:
                        return x
                    break
        else:
            return -1
       
        
"""class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Build the frequency map
        # This takes O(n) time
        count_map = {}
        for char in s:
            count_map[char] = count_map.get(char, 0) + 1
        
        # Step 2: Iterate through the string to find the first unique
        # This also takes O(n) time
        for index in range(len(s)):
            if count_map[s[index]] == 1:
                return index
        
        # If no unique character exists
        return -1   """     