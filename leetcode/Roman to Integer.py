class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50,
             "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s) - 1):
            if s[i] in d.keys():
                value = d.get(s[i])
                next_value = d.get(s[i + 1])
                if value < next_value:
                    total -= value
                else:
                    total += value    
        total += d[s[-1]]      
        return total  
                    
                    
            
result = Solution()
print(result.romanToInt("MCMXCIV"))        