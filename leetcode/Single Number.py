from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) ->int:
        result = 0
        for i in nums:
            result ^= i
        return result                
                
# result = Solution()
# print(result.singleNumber(nums = list(map(int, input().split()))))           
                