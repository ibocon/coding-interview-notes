# 백준 1918번 후위표기식

import sys
rl = sys.stdin.readline

priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
stack = []
for c in '(' + rl().rstrip() + ')':
    if 'A' <= c <= 'Z':
        print(c, end='')
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while True:
            item = stack.pop()
            if item == '(':
                break
            print(item, end='')
    else:
        while stack[-1] != '(' and priority[c] <= priority[stack[-1]]:
            print(stack.pop(), end='')
        stack.append(c)
