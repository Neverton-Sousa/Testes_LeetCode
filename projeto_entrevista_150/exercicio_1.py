# Você recebe duas matrizes inteiras nums1e nums2, classificadas em ordem não decrescente , e dois inteiros me n, representando o número de elementos em nums1e, nums2respectivamente.
# Mesclar nums1 e nums2em uma única matriz classificada em ordem não decrescente .
# O array classificado final não deve ser retornado pela função, mas sim armazenado dentro do arraynums1 . Para acomodar isso, nums1tem um comprimento de m + n, onde os primeiros melementos denotam os elementos que devem ser mesclados e os últimos nelementos são definidos 0e devem ser ignorados. nums2tem um comprimento de n.

# Exemplo 1:
# Entrada: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#  Saída: [1,2,2,3,5,6]
#  Explicação: Os arrays que estamos mesclando são [1,2,3] e [2,5,6].
# O resultado da mesclagem é [ 1 , 2 ,2, 3 ,5,6] com os elementos sublinhados vindos de nums1.

# Exemplo 2:
# Entrada: nums1 = [1], m = 1, nums2 = [], n = 0
#  Saída: [1]
#  Explicação: As matrizes que estamos mesclando são [1] e [].
# O resultado da mesclagem é [1].

# Exemplo 3:
# Entrada: nums1 = [0], m = 0, nums2 = [1], n = 1
#  Saída: [1]
#  Explicação: Os arrays que estamos mesclando são [] e [1].
# O resultado da mesclagem é [1].
# Observe que como m = 0, não há elementos em nums1. O 0 existe apenas para garantir que o resultado da mesclagem caiba em nums1.


def merge(nums1, m, nums2, n):
    for j in range(n):
        nums1[m + j] = nums2[j]
    nums1.sort()


nums1 = [[1, 2, 3, 0, 0, 0], [1], [0]]
m = [3, 1, 0]
nums2 = [[2, 5, 6], [], [1]]
n = [3, 0, 1]
for i in range(3):

    merge(nums1[i], m[i], nums2[i], n[i])
