# Dado um array inteiro numse um inteiro val, remova todas as ocorrências de valin nums -place . A ordem dos elementos pode ser alterada. Em seguida, retorne o número de elementos em numsque não são iguais aval .

# Considere o número de elementos em numsque não são iguais a valbe k, para ser aceito, você precisa fazer o seguinte:

# Altere a matriz numsde forma que os primeiros kelementos numscontenham os elementos que não são iguais a val. Os elementos restantes de numsnão são importantes, assim como o tamanho de nums.
# Retornar k.
# Juiz Personalizado:

# O juiz testará sua solução com o seguinte código:

# int[] números = [...]; //matriz de entrada
# valor interno = ...; //Valor a ser removido
# int[] Nums esperados = [...]; // A resposta esperada com comprimento correto.
#                             // É classificado sem valores iguais a val.

# int k = removeElement(nums, val); // Chama sua implementação

# afirmar k == esperadoNums.length;
# ordenar(números, 0, k); //Ordena os primeiros k elementos de nums
# for (int i = 0; i < comprimento real; i++) {
#     afirmar nums[i] == esperadoNums[i];
# }
# Se todas as afirmações forem aprovadas, sua solução será aceita .


# Exemplo 1:

# Entrada: nums = [3,2,2,3], val = 3
#  Saída: 2, nums = [2,2,_,_]
#  Explicação: Sua função deve retornar k = 2, com os dois primeiros elementos de nums sendo 2.
# Não importa o que você deixa além do k retornado (portanto, eles são sublinhados).
# Exemplo 2:

# Entrada: nums = [0,1,2,2,3,0,4,2], val = 2
#  Saída: 5, nums = [0,1,4,0,3,_,_,_]
#  Explicação: Sua função deve retornar k = 5, com os primeiros cinco elementos de nums contendo 0, 0, 1, 3 e 4.
# Observe que os cinco elementos podem ser retornados em qualquer ordem.
# Não importa o que você deixa além do k retornado (portanto, eles são sublinhados).


def removeElement(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


listas = [[3, 2, 2, 3], [0, 1, 2, 2, 3, 0, 4, 2]]
vals = [3, 2]
for i in range(2):

    print(removeElement(listas[i], vals[i]))
