def maxDepth(s):
    profundidade = 0
    max_profundidade = 0

    for char in s:
        if char == "(":
            profundidade += 1
            if profundidade > max_profundidade:
                max_profundidade = profundidade
        elif char == ")":
            profundidade -= 1

    return max_profundidade


VPS = ["(1+(2*3)+((8)/4))+1", "(1)+((2))+(((3)))"]
for i in VPS:
    print(maxDepth(i))
