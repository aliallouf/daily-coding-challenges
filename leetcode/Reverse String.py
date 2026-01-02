class Solution:
    def reverseString(self, s: list[str]) -> None:
        # The [:] tells Python to replace the contents 
        # of the original list with the reversed version.
        s[:] = s[::-1]
        
        
result = Solution()
result.reverseString(["h","e","l","l","o"])        
"""
        The Two-Pointer Approach
        How it works:

Place one pointer (left) at the beginning and one (right) at the end.

Swap the characters at these positions.

Move the pointers toward each other until they meet in the middle.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap elements
            s[left], s[right] = s[right], s[left]
            # Move pointers
            left += 1
            right -= 1
    """