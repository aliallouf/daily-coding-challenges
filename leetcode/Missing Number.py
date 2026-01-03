class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n + 1):
            if i not in nums:
                print(i)
            
result = Solution()
result.missingNumber([9,6,4,2,3,5,7,0,1])            

"""
XORing a number with itself results in 0. By XORing all indices and all values in the list,
the "pairs" cancel out, leaving only the missing number.
    class Solution:
        def missingNumber(self, nums: List[int]) -> int:
            missing = len(nums)
            for i, num in enumerate(nums):
                missing ^= i ^ num
            return missing
XOR Time Complexity: O(n) Space Complexity: O(1)        
    """