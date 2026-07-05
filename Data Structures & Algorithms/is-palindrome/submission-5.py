class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1

            if s[left].lower() != s[right].lower():
                return False
        
            left+=1
            right-=1
        return True

"""
I use two pointers.

One starts from the left side, and one starts from the right side.

I skip spaces and special characters.

Then I compare the two letters in lowercase.

If they are different, I return false.

If they are the same, I move both pointers inward.

If there is no mismatch, I return true.

The time complexity is O(n), and the space complexity is O(1).


"""

        