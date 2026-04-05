class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={')':'(','}':'{',']':'['}

        for ch in s:
            if ch not in mapping:
                stack.append(ch)
            else:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                else:
                    stack.pop()
        return not stack
'''
I use a stack to store opening brackets.
I iterate through the string, and if the character is not in the mapping, I treat it as an opening bracket and push it onto the stack.
If it is a closing bracket, I check whether the stack is empty or whether the top of the stack does not match the corresponding opening bracket in the mapping. If either condition is true, I return false.
Otherwise, I pop the stack.
Finally, if the stack is empty, I return true.
'''

        