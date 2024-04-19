class Solution(object):
    def isValid(self, s):

        open_close_patentheses = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in open_close_patentheses:
                if stack and stack[-1] == open_close_patentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False



