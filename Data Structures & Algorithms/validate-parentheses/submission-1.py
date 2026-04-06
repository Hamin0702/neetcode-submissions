class Solution:
    def isValid(self, s: str) -> bool:
        
        #EC: when it starts with closing bracket then it's never a valid parantheses
        if s[0] in [")", "]", "}"]:
            return False

        stack = []

        for c in s:
            if len(stack) > 0 and c == ")" and stack[-1] == "(":
                stack.pop()
            elif len(stack) > 0 and c == "}" and stack[-1] == "{":
                stack.pop()    
            elif len(stack) > 0 and c == "]" and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0 