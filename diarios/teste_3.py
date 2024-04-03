# Dada uma m x ngrade de caracteres boarde uma string word, retorne true se word existir na grade .

# A palavra pode ser construída a partir de letras de células adjacentes sequencialmente, onde as células adjacentes são vizinhas horizontal ou verticalmente. A mesma célula de letra não pode ser usada mais de uma vez.

# Entrada: placa = [["A","B","C","E"],["S","F","C","S"],["A","D", "E","E"]], palavra = "ABCCED"
#  Saída: verdadeiro

# Entrada: placa = [["A","B","C","E"],["S","F","C","S"],["A","D", "E","E"]], palavra = "VER"
#  Saída: verdadeiro

# Entrada: placa = [["A","B","C","E"],["S","F","C","S"],["A","D", "E","E"]], palavra = "ABCB"
#  Saída: falso

# Restrições:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# boarde wordconsiste apenas em letras inglesas minúsculas e maiúsculas.


def existe_palavra(board, word):
    # Função auxiliar para verificar se é possível encontrar a palavra a partir de uma posição específica
    def dfs(i, j, k):
        # Verifica se a posição está dentro dos limites da matriz
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return False
        # Verifica se a letra na posição atual é igual à letra na palavra na posição k
        if board[i][j] != word[k]:
            return False
        # Se a palavra inteira foi encontrada, retorna True
        if k == len(word) - 1:
            return True
        # Marca a célula atual como visitada
        temp = board[i][j]
        board[i][j] = ""
        # Verifica as células vizinhas
        found = (
            dfs(i + 1, j, k + 1)
            or dfs(i - 1, j, k + 1)
            or dfs(i, j + 1, k + 1)
            or dfs(i, j - 1, k + 1)
        )
        # Restaura a célula para o seu valor original
        board[i][j] = temp
        return found

    # Percorre toda a matriz
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Se a primeira letra da palavra for encontrada na posição (i, j), chama dfs para verificar se a palavra completa pode ser encontrada
            if dfs(i, j, 0):
                return True
    return False


# Teste
matriz = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
palavras = ["ABCCED", "SEE", "ABCB"]
for palavra in palavras:
    print(existe_palavra(matriz, palavra))  # Saída: True
