class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            # If the current number matches our candidate, increment
            # Otherwise, decrement (the "fight" logic)
            count += (1 if num == candidate else -1)

        return candidate    
           
res = Solution()
print(res.majorityElement([3,2,3]))                    