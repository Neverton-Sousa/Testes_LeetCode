class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        j = word.find(ch)
        if j != -1:
            return word[: j + 1][::-1] + word[j + 1 :]
        return word


# 2000. Prefixo reverso do Word
# Resolvido
# Fácil
# Tópicos
# Empresas
# Dica
# Dada uma string indexada em 0word e um caractere ch, inverta o segmento wordque começa no índice 0e termina no índice da primeira ocorrência de ch( inclusive ). Se o personagem chnão existir em word, não faça nada.

# Por exemplo, se word = "abcdefd"e ch = "d", então você deve inverter o segmento que começa 0e termina em 3( inclusive ). A sequência resultante será ."dcbaefd"
# Retorne a string resultante .


# Exemplo 1:

# Entrada: word = " abcd efd", ch = "d"
#  Saída: " dcba efd"
#  Explicação:  A primeira ocorrência de "d" está no índice 3.
# Inverta a parte da palavra de 0 a 3 (inclusive), a string resultante é "dcbaefd".
# Exemplo 2:

# Entrada: word = " xyxz xe", ch = "z"
#  Saída: " zxyx xe"
#  Explicação:  A primeira e única ocorrência de "z" está no índice 3.
# Inverta a parte da palavra de 0 a 3 (inclusive), a string resultante é "zxyxxe".
# Exemplo 3:

# Entrada: word = "abcd", ch = "z"
#  Saída: "abcd"
#  Explicação:  "z" não existe no word.
# Você não deve fazer nenhuma operação reversa, a string resultante é "abcd".
