# Dada uma string scomposta por palavras e espaços, retorne o comprimento da última palavra da string.

# Uma palavra é um máximo
# substring
# consistindo apenas em caracteres sem espaço.

# Exemplo 1:
# Entrada: s = "Hello World"
#  Saída: 5
#  Explicação: A última palavra é "World" com comprimento 5.

# Exemplo 2:
# Entrada: s = "voe-me para a lua"
#  Saída: 4
#  Explicação: A última palavra é "lua" com comprimento 4.

# Exemplo 3:
# Entrada: s = "luffy ainda é joyboy"
#  Saída: 6
#  Explicação: A última palavra é "joyboy" com comprimento 6.


def lengthOfLastWord(s):
    palavras = s.strip().split(" ")

    return len(palavras[-1])


testes = ["Hello World", " Me faça voar até a lua ", "Luffy ainda é Joyboy"]
for i in testes:
    print(lengthOfLastWord(i))
