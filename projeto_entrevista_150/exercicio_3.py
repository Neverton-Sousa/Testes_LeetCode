def removeDuplicates(nums):

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


# Dada uma matriz inteira numsclassificada em ordem não decrescente , remova as duplicatas no local de forma que cada elemento exclusivo apareça apenas uma vez . A ordem relativa dos elementos deve ser mantida a mesma . Em seguida, retorne o número de elementos únicos emnums .
# Considere o número de elementos únicos de numsto be k. Para ser aceito, você precisa fazer o seguinte:
# Altere a matriz numsde forma que os primeiros kelementos numscontenham os elementos únicos na ordem em que estavam presentes numsinicialmente. Os elementos restantes de numsnão são importantes, assim como o tamanho de nums.
# Retornar k.
# Juiz Personalizado:

# O juiz testará sua solução com o seguinte código:

# int[] números = [...]; //matriz de entrada
# int[] Nums esperados = [...]; //A resposta esperada com comprimento correto

# int k = removeDuplicados(nums); // Chama sua implementação

# afirmar k == esperadoNums.length;
# for (int i = 0; i < k; i++) {
#     afirmar nums[i] == esperadoNums[i];
# }
# Se todas as afirmações forem aprovadas, sua solução será aceita .

# Exemplo 1:
# Entrada: nums = [1,1,2]
#  Saída: 2, nums = [1,2,_]
#  Explicação: Sua função deve retornar k = 2, com os dois primeiros elementos de nums sendo 1 e 2 respectivamente.
# Não importa o que você deixa além do k retornado (portanto, eles são sublinhados).

# Exemplo 2:
# Entrada: nums = [0,0,1,1,1,2,2,3,3,4]
#  Saída: 5, nums = [0,1,2,3,4,_,_,_,_, _]
#  Explicação: Sua função deve retornar k = 5, com os primeiros cinco elementos de nums sendo 0, 1, 2, 3 e 4 respectivamente.
# Não importa o que você deixa além do k retornado (portanto, eles são sublinhados).
