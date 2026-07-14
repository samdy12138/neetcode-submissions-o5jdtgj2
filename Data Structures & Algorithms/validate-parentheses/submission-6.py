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
I use a stack.

If I see an opening bracket, I put it into the stack.

If I see a closing bracket, I check if it matches the top of the stack.

If it does not match, I return false. If it matches, 
I remove the top bracket.

At the end, the stack should be empty.

The time complexity is O(n).


"""

        
        