class Solution:
    def isValid(self, s: str) -> bool:
        mapping={")":"(","}":"{","]":"["}
        stack=[]
        for ch in s:
            if ch not in mapping:
                stack.append(ch)
            else:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                else:
                    stack.pop() 
        return not stack

"""
I use a stack to store opening brackets.

When I see an opening bracket, I push it into the stack. 
When I see a closing bracket, I check whether it matches the bracket
 at the top of the stack.

If it does not match, I return false. If it matches, I pop the stack.

At the end, the string is valid only if the stack is empty.

The time complexity is O(n), and the space complexity is O(n).

"""

        
        