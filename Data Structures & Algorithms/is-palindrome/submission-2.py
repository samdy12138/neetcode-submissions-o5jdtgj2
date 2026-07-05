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
I use two pointers, one from the left and one from the right. 
I skip all non-alphanumeric characters on both sides. 
Then I compare the lowercase version of the two characters.

If they are not equal, I return false. If they are equal, 
I move both pointers inward. If the loop finishes, 
it means the string is a valid palindrome.

The time complexity is O(n), and the space complexity is O(1).

"""

        