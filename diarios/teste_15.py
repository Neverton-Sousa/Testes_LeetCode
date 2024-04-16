# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 1:
            return TreeNode(val=val, left=root)

        def dfs(node, level):
            if level == depth - 1:
                node.left = (
                    TreeNode(val, left=node.left) if node.left else TreeNode(val)
                )
                node.right = (
                    TreeNode(val, right=node.right) if node.right else TreeNode(val)
                )
                return node
            else:
                if node.left:
                    node.left = dfs(node.left, level + 1)
                if node.right:
                    node.right = dfs(node.right, level + 1)
                return node

        root = dfs(root, 1)
        return root


# Dado o valor rootde uma árvore binária e dois inteiros vale depth, adicione uma linha de nós com valor valna profundidade fornecida depth.

# Observe que o rootnó está em profundidade 1.

# A regra de adição é:

# Dado o número inteiro depth, para cada nó de árvore não nulo curna profundidade depth - 1, crie dois nós de árvore com valor valcomo curraiz esquerda da subárvore e raiz direita da subárvore.
# curA subárvore esquerda original de deve ser a subárvore esquerda da nova raiz da subárvore esquerda.
# curA subárvore direita original deve ser a subárvore direita da nova raiz da subárvore direita.
# Se depth == 1isso significa que não há profundidade depth - 1alguma, crie um nó de árvore com valor valcomo a nova raiz de toda a árvore original, e a árvore original será a subárvore esquerda da nova raiz.


# Exemplo 1:


# Entrada: raiz = [4,2,6,3,1,5], val = 1, profundidade = 2
#  Saída: [4,1,1,2,null,null,6,3,1,5]
# Exemplo 2:


# Entrada: raiz = [4,2,null,3,1], val = 1, profundidade = 3
#  Saída: [4,2,null,1,1,3,null,null,1]
