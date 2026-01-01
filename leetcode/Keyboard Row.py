class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # 1. Create a full mapping of every letter to its row number
        # We can do this efficiently using a dictionary comprehension
        row_map = {}
        for char in "qwertyuiop": row_map[char] = 1
        for char in "asdfghjkl": row_map[char] = 2
        for char in "zxcvbnm":    row_map[char] = 3
        
        valid_words = []
        
        for word in words:
            # Convert to lowercase once per word to handle case-insensitivity
            lower_word = word.lower()
            
            # 2. Determine which row the first letter belongs to
            target_row = row_map[lower_word[0]]
            
            # 3. Check if all other letters in the word are in the same row
            is_single_row = True
            for char in lower_word:
                if row_map[char] != target_row:
                    is_single_row = False
                    break
            
            # 4. If the loop finished without finding a different row, keep it
            if is_single_row:
                valid_words.append(word)
                
        return valid_words
"""class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # Define the three rows clearly
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            # 1. Convert the word to lowercase and make it a set of letters
            # "Dad" becomes {'d', 'a'}
            word_set = set(word.lower())
            
            # 2. Check if the word_set is a subset of any keyboard row
            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
                result.append(word)
                
        return result

# Test
sol = Solution()
print(sol.findWords(["Hello", "Alaska", "Dad", "Peace"])) 
# Output: ['Alaska', 'Dad']
        """