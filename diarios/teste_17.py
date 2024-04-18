class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2

        return perimeter


# Você recebe row x col grida representação de um mapa onde grid[i][j] = 1representa a terra e grid[i][j] = 0representa a água.

# As células da grade são conectadas horizontalmente/verticalmente (não diagonalmente). O gridestá completamente cercado por água e há exatamente uma ilha (ou seja, uma ou mais células terrestres conectadas).

# A ilha não possui “lagos”, o que significa que a água de seu interior não está ligada à água ao redor da ilha. Uma célula é um quadrado com comprimento lateral 1. A grade é retangular, a largura e a altura não excedem 100. Determine o perímetro da ilha.


# Exemplo 1:


# Entrada: grade = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
#  Saída: 16
#  Explicação: O perímetro são as 16 listras amarelas da imagem acima.
# Exemplo 2:

# Entrada: grade = [[1]]
#  Saída: 4
# Exemplo 3:

# Entrada: grade = [[1,0]]
#  Saída: 4
