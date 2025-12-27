class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            num_list = list(map(int, str(n)))
            n = sum(i **2 for i in num_list)
            # Check if we have seen this number before
            if n in seen:
                return False
            seen.add(n)
        return True     



"""class Solution:
    def isHappy(self, n: int) -> bool:
        # 1. Create a set to track numbers we have already seen
        seen = set()
        
        # 2. Loop until n becomes 1 (Happy) or we hit a number we've seen (Sad/Loop)
        while n != 1 and n not in seen:
            seen.add(n)
            
            # --- Your original logic starts here ---
            num_list = list(map(int, str(n)))
            result = 0
            for i in num_list:
                result += i ** 2
            # --- Your original logic ends here ---
            
            # Update n with the new result for the next iteration
            n = result
            
        # 3. If the loop ended because n is 1, return True. Otherwise False.
        return n == 1

# Testing the code
result_obj = Solution()
print(f"Is 19 happy? {result_obj.isHappy(19)}")
print(f"Is 2 happy? {result_obj.isHappy(2)}")"""