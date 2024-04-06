def minRemoveToMakeValid(s):
    openParenthesesCount = 0
    arr = list(s)

    for i in range(len(arr)):
        if arr[i] == "(":
            openParenthesesCount += 1
        elif arr[i] == ")":
            if openParenthesesCount == 0:
                arr[i] = "*"
            else:
                openParenthesesCount -= 1

    for i in range(len(arr) - 1, -1, -1):
        if openParenthesesCount > 0 and arr[i] == "(":
            arr[i] = "*"
            openParenthesesCount -= 1

    result = "".join(c for c in arr if c != "*")

    return result


print(minRemoveToMakeValid("lee(t(c)o)de)"))
print(minRemoveToMakeValid("a)b(c)d"))
print(minRemoveToMakeValid("))(("))
