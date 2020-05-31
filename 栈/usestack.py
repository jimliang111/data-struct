"""
leetcode no.20
"""


def isValid(s: str) -> bool:
    stack = []
    left = '({['
    for c in s:
        if c in left:
            stack.append(c)
        else:
            top = stack.pop() if len(stack) else ''
            if not top:
                return False
            elif c == ')' and top != '(':
                return False
            elif c == '}' and top != '{':
                return False
            elif c == ']' and top != '[':
                return False
    return len(stack) == 0


if __name__ == '__main__':
    s = '()'
    print(isValid(s))
