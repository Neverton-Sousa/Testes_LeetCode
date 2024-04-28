from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        positions = defaultdict(list)
        for i, c in enumerate(ring):
            positions[c].append(i)
        return self.helper(0, 0, positions, key, ring, memo)

    def helper(self, in_index, pos, positions, key, ring, memo):
        if in_index == len(key):
            return 0
        if (in_index, pos) in memo:
            return memo[(in_index, pos)]
        min_steps = float("inf")
        for i in positions[key[in_index]]:
            if i >= pos:
                steps = min(i - pos, pos + len(ring) - i)
            else:
                steps = min(pos - i, i + len(ring) - pos)
            min_steps = min(
                min_steps,
                steps + self.helper(in_index + 1, i, positions, key, ring, memo),
            )
        memo[(in_index, pos)] = min_steps + 1
        return min_steps + 1


# 514. Trilha da Liberdade
# Resolvido
# Duro
# Tópicos
# Empresas
# No videogame Fallout 4, a missão "Road to Freedom" exige que os jogadores alcancem um mostrador de metal chamado "Freedom Trail Ring" e usem o mostrador para soletrar uma palavra-chave específica para abrir a porta.

# Dada uma string ringque representa o código gravado no anel externo e outra string keyque representa a palavra-chave que precisa ser escrita, retorne o número mínimo de etapas para escrever todos os caracteres da palavra-chave .

# Inicialmente, o primeiro caractere do anel é alinhado na "12:00"direção. Você deve soletrar todos os caracteres keyum por um girando ringno sentido horário ou anti-horário para alinhar cada caractere da tecla de string na "12:00"direção e, em seguida, pressionando o botão central.

# Na fase de girar o anel para soletrar o personagem-chave key[i]:

# Você pode girar o anel no sentido horário ou anti-horário em uma posição, o que conta como um passo . O objetivo final da rotação é alinhar um dos ringcaracteres na "12:00"direção em que esse caractere deve ser igual a key[i].
# Se o personagem key[i]estiver alinhado na "12:00"direção, pressione o botão central para soletrar, o que também conta como um passo . Após pressionar, você poderá começar a soletrar o próximo caractere da tecla (próximo estágio). Caso contrário, você terminou toda a ortografia.


# Exemplo 1:


# Entrada: ring = "godding", key = "gd"
#  Saída: 4
#  Explicação:
# Para o primeiro caractere chave 'g', uma vez que já está instalado, precisamos apenas de 1 passo para soletrar esse caractere.
# Para o segundo caractere chave 'd', precisamos girar o anel "godding" no sentido anti-horário em dois passos para torná-lo "ddinggo".
# Além disso, precisamos de mais 1 etapa para ortografia.
# Portanto, a saída final é 4.
# Exemplo 2:

# Entrada: ring = "godding", key = "godding"
#  Saída: 13
