from stack import Stack


class Balance:

    def check_balance(self, items, brackets='〈〉()[]{}'):
        opening = brackets[::2]
        closing = brackets[1::2]
        stack = Stack()
        for sym in items:
            if sym in opening:
                stack.push(opening.index(sym))
            elif sym in closing:
                if stack.stack and stack.peek() == closing.index(sym):
                    stack.pop()
                else:
                    return False
        return not stack.stack


