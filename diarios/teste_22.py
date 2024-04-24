class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Initialize the adjacency list and degree of each node
        adjacency_list = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Initialize leaves queue
        leaves = deque([i for i in range(n) if degree[i] == 1])

        # Trim leaves until 2 or fewer nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in adjacency_list[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)


# 310. Árvores de Altura Mínima
# Resolvido
# Médio
# Tópicos
# Empresas
# Dica
# Uma árvore é um grafo não direcionado no qual dois vértices quaisquer estão conectados por  exatamente  um caminho. Em outras palavras, qualquer grafo conectado sem ciclos simples é uma árvore.

# Dada uma árvore de nnós rotulada de 0até n - 1e uma matriz de  n - 1 edgesonde indica que há uma aresta não direcionada entre os dois nós  e  na árvore, você pode escolher qualquer nó da árvore como raiz. Quando você seleciona um nó como raiz, a árvore resultante tem altura . Entre todas as árvores com raízes possíveis, aquelas com altura mínima (ou seja ) são chamadas de árvores de altura mínima (MHTs).edges[i] = [ai, bi]aibixhmin(h)

# Retorne uma lista de todos os rótulos raiz dos MHTs . Você pode retornar a resposta em qualquer ordem .

# A altura de uma árvore enraizada é o número de arestas no caminho descendente mais longo entre a raiz e uma folha.


# Exemplo 1:


# Entrada: n = 4, arestas = [[1,0],[1,2],[1,3]]
#  Saída: [1]
#  Explicação: Como mostrado, a altura da árvore é 1 quando a raiz é o nó com rótulo 1 que é o único MHT.
# Exemplo 2:


# Entrada: n = 6, arestas = [[3,0],[3,1],[3,2],[3,4],[5,4]]
#  Saída: [3,4]
