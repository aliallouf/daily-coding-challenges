class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums.reverse()
        def helper(start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        helper(0, k-1)    
        helper(k, n - 1)    
   
            
            
result = Solution()
result.rotate([1,2,3,4,5,6,7],3)        