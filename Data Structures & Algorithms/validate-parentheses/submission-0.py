class Solution:
    def isValid(self, s: str) -> bool:
        close_open={")":"(","}":"{","]":"["}
        stack : list[str] = []
        for chr in s:
            if chr not in close_open:
                stack.append(chr)
                continue
            if len(stack) == 0:
                return False
            if stack.pop() != close_open[chr]:
                return False
        return len(stack) == 0