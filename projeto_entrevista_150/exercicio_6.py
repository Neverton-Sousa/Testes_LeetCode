def rotate(nums, k):
    for i in range(k):
        nums.insert(0, nums.pop(-1))


rotate([1, 2, 3, 4, 5, 6, 7], 3)

rotate([-1, -100, 3, 99], 2)


# Dado um array inteiro nums, gire o array para a direita em ketapas, onde ké não negativo.


# Exemplo 1:

# Entrada: nums = [1,2,3,4,5,6,7], k = 3
#  Saída: [5,6,7,1,2,3,4]
#  Explicação:
# gire 1 passo para a direita: [7,1,2,3,4,5,6]
# gire 2 passos para a direita: [6,7,1,2,3,4,5]
# gire 3 passos para a direita: [5,6,7,1,2,3,4]
# Exemplo 2:

# Entrada: nums = [-1,-100,3,99], k = 2
#  Saída: [3,99,-1,-100]
#  Explicação:
# gire 1 passo para a direita: [99,-1,-100,3]
# gire 2 passos para a direita: [3,99,-1,-100]


# Restrições:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
