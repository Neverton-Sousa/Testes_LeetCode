class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            return False

        visited = set()
        return dfs(source, visited)


# Existe um gráfico bidirecional com nvértices, onde cada vértice é rotulado de 0até n - 1( inclusive ). As arestas no gráfico são representadas como uma matriz de inteiros 2D edges, onde cada uma denota uma aresta bidirecional entre vértice e vértice . Cada par de vértices é conectado por no máximo uma aresta, e nenhum vértice possui uma aresta própria.edges[i] = [ui, vi]uivi

# Você deseja determinar se existe um caminho válido de vértice sourcea vértice destination.

# Dado edgese os números inteiros n, sourcee destination, retornam truese houver um caminho válido de sourcepara destination, ou falsecaso contrário .


# Exemplo 1:


# Entrada: n = 3, arestas = [[0,1],[1,2],[2,0]], origem = 0, destino = 2
#  Saída: verdadeiro
#  Explicação: Existem dois caminhos do vértice 0 ao vértice 2 :
# - 0 → 1 → 2
# - 0 → 2
# Exemplo 2:


# Entrada: n = 6, arestas = [[0,1],[0,2],[3,5],[5,4],[4,3]], origem = 0, destino = 5
#  Saída: falso
#  Explicação: Não há caminho do vértice 0 ao vértice 5.
