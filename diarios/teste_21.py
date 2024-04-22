class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Convert deadends to a set for O(1) lookup
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        # Initialize BFS
        queue = deque([("0000", 0)])  # (current_combination, moves)
        visited = set("0000")

        # BFS loop
        while queue:
            current_combination, moves = queue.popleft()

            # Check if we've reached the target
            if current_combination == target:
                return moves

            # Generate next possible combinations
            for i in range(4):
                for delta in [-1, 1]:
                    new_digit = (int(current_combination[i]) + delta) % 10
                    new_combination = (
                        current_combination[:i]
                        + str(new_digit)
                        + current_combination[i + 1 :]
                    )

                    # Check if the new combination is valid and not visited
                    if (
                        new_combination not in visited
                        and new_combination not in deadends
                    ):
                        visited.add(new_combination)
                        queue.append((new_combination, moves + 1))

        # If target is not reachable
        return -1


# Você tem uma fechadura à sua frente com 4 rodas circulares. Cada roda possui 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. As rodas podem girar livremente e girar: por exemplo, podemos virar '9'para ser '0'ou '0'para ser '9'. Cada movimento consiste em girar uma roda em um slot.

# O bloqueio começa inicialmente em '0000', uma string que representa o estado das 4 rodas.

# Você recebe uma lista de deadendsbecos sem saída, o que significa que se a fechadura exibir algum desses códigos, as rodas da fechadura pararão de girar e você não conseguirá abri-la.

# Dado um targetrepresentando o valor das rodas que irão destravar a fechadura, retorne o número total mínimo de voltas necessárias para abrir a fechadura, ou -1 se for impossível.


# Exemplo 1:

# Entrada: becos sem saída = ["0201","0101","0102","1212","2002"], alvo = "0202"
#  Saída: 6
#  Explicação:
# Uma sequência de movimentos válidos seria "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Observe que uma sequência como "0000" -> "0001" -> "0002" -> "0102" -> "0202" seria inválida,
# porque as rodas da fechadura ficam presas depois que o display se torna o beco sem saída "0102".
# Exemplo 2:

# Entrada: becos sem saída = ["8888"], alvo = "0009"
#  Saída: 1
#  Explicação: Podemos girar a última roda ao contrário para passar de "0000" -> "0009".
# Exemplo 3:

# Entrada: becos sem saída = ["8887","8889","8878","8898","8788","8988","7888","9888"], alvo = "8888"
#  Saída: -1
#  Explicação: Nós não consegue atingir o alvo sem ficar preso.
