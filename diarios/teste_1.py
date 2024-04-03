# Número binário ímpar máximo

# Você recebe uma string binárias que contém pelo menos um arquivo '1'.
# Você deve reorganizar os bits de forma que o número binário resultante seja o número binário ímpar máximo que pode ser criado a partir dessa combinação.
# Retorna uma string representando o número binário ímpar máximo que pode ser criado a partir de uma determinada combinação.
# Observe que a string resultante pode ter zeros à esquerda.

# Exemplo 1:
# Entrada: s = "010"
# Saída: "001"
# Explicação: Como existe apenas um '1', ele deve estar na última posição. Então a resposta é "001".

# Exemplo 2:
# Entrada: s = "0101"
# Saída: "1001"
# Explicação: Um dos '1's deve estar na última posição. O número máximo que pode ser formado com os dígitos restantes é “100”. Portanto a resposta é “1001”.


def maximumOddBinaryNumber(s):
    uns = s.count("1")
    total = len(s)
    if uns != 1:
        final = "1" * (uns - 1) + "0" * (total - uns) + "1"
    else:
        final = "0" * (total - uns) + "1"
    return final


s = "010"
print(maximumOddBinaryNumber(s))
