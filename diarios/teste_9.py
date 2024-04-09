def timeRequiredToBuy(tickets, k):
    total = 0
    for i, x in enumerate(tickets):
        if i <= k:
            total += min(tickets[i], tickets[k])
        else:
            total += min(tickets[i], tickets[k] - 1)

    return total


print(timeRequiredToBuy([2, 3, 2], 2))

print(timeRequiredToBuy([5, 1, 1, 1], 0))


# Tem ngente fazendo fila para comprar ingresso, onde a pessoa fica na frente e a pessoa no final da fila.0th(n - 1)th
# Você recebe uma matriz inteira indexada em 0tickets de comprimento, nonde o número de ingressos que a pessoa gostaria de comprar é .ithtickets[i]
# Cada pessoa leva exatamente 1 segundo para comprar um ingresso. Uma pessoa só pode comprar 1 ingresso por vez e tem que voltar até o final da fila (o que acontece instantaneamente ) para poder comprar mais ingressos. Se a pessoa não tiver mais ingressos para comprar, ela sairá da fila.
# Retorne o tempo que a pessoa na posição (indexada 0) levou para finalizar a compra dos ingressos .k

# Exemplo 1:
# Entrada: tickets = [2,3,2], k = 2
#  Saída: 6
#  Explicação:
# - Na primeira passagem, todos na fila compram um ingresso e a fila vira [1, 2, 1].
# - Na segunda passagem, todos na fila compram um ingresso e a fila passa a ser [0, 1, 0].
# A pessoa na posição 2 comprou 2 ingressos com sucesso e demorou 3 + 3 = 6 segundos.
# Exemplo 2:

# Entrada: tickets = [5,1,1,1], k = 0
#  Saída: 8
#  Explicação:
# - Na primeira passagem, todos na fila compram um ingresso e a fila passa a ser [4, 0, 0, 0].
# - Nas próximas 4 passagens, apenas quem está na posição 0 está comprando ingressos.
# A pessoa na posição 0 comprou 5 ingressos com sucesso e demorou 4 + 1 + 1 + 1 + 1 = 8 segundos.


# Restrições:

# n == tickets.length
# 1 <= n <= 100
# 1 <= tickets[i] <= 100
# 0 <= k < n
