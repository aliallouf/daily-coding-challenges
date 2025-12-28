class Solution:
    def containDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

"""seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
"""
"""The One-Liner: Set Length Comparison
In Python, you can compare the length of the original list with the length of a set created from that list. 
If the lengths are different, a duplicate was removed.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
Pros: Extremely concise.

Cons: It always traverses the entire list, 
whereas the "Optimized Approach" above can return True early as soon as it finds the first duplicate.
"""         
           
    
result = Solution()
print(result.containDuplicate([1])) 

        