class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "}" : "{",
            ")" : "(",
            "]" : "[",
        }
        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != mapping.get(char):
                    return False
        return len(stack) == 0

        

        