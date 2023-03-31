def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
    return max_len


s = input()
print(longest_valid_parentheses(s))