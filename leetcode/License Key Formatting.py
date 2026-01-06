class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 1. Clean the string: remove dashes, uppercase everything, and reverse it
        # We reverse it first so we can group by k from right-to-left
        clean_s = s.replace("-", "").upper()[::-1]
        
        result_list = []
        count = 0
        
        # 2. Iterate through the cleaned characters
        for char in clean_s:
            result_list.append(char)
            count += 1
            
            # 3. Every k characters, add a dash
            if count == k:
                result_list.append('-')
                count = 0
        
        # 4. Cleanup: If the last character added was a dash, remove it
        # This happens if the total number of characters is a multiple of k
        if result_list and result_list[-1] == '-':
            result_list.pop()
            
        # 5. Reverse it back to the original order and join into a string
        return "".join(result_list[::-1])

# Testing the logic
result = Solution()
print(result.licenseKeyFormatting("2-5g-3-J", 2))  # Output: "2-5G-3J"
print(result.licenseKeyFormatting("5F3Z-2e-9-w", 4)) # Output: "5F3Z-2E9W"