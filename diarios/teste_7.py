def checkValidString(s):
    leftMin, leftMax = 0, 0

    for c in s:
        if c == "(":
            leftMin, leftMax = leftMin + 1, leftMax + 1
        elif c == ")":
            leftMin, leftMax = leftMin - 1, leftMax - 1
        else:
            leftMin, leftMax = leftMin - 1, leftMax + 1
        if leftMax < 0:
            return False
        if leftMin < 0:
            leftMin = 0
    return leftMin == 0


print(checkValidString("()"))
print(checkValidString("(*)"))
print(checkValidString("(*))"))


# Dada uma string scontendo apenas três tipos de caracteres: '('e ')', '*'retorne true se s for válido .

# As regras a seguir definem uma string válida :

# Qualquer parêntese esquerdo '('deve ter um parêntese direito correspondente ')'.
# Qualquer parêntese direito ')'deve ter um parêntese esquerdo correspondente '('.
# O parêntese esquerdo '('deve vir antes do parêntese direito correspondente ')'.
# '*'pode ser tratado como um único parêntese direito ')'ou um único parêntese esquerdo '('ou uma string vazia "".


# Exemplo 1:

# Entrada: s = "()"
#  Saída: verdadeiro
# Exemplo 2:

# Entrada: s = "(*)"
#  Saída: verdadeiro
# Exemplo 3:

# Entrada: s = "(*))"
#  Saída: verdadeiro
