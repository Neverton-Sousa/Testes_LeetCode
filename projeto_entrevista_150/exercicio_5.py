def majorityElement(nums):
    unicos = sorted(set(nums))
    for i in unicos:
        if nums.count(i) > len(nums) / 2:
            return i


print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))


# Dado um array numsde tamanho n, retorne o elemento majoritário .

# O elemento majoritário é aquele que aparece mais de ⌊n / 2⌋uma vez. Você pode assumir que o elemento majoritário sempre existe na matriz.


# Exemplo 1:

# Entrada: nums = [3,2,3]
#  Saída: 3
# Exemplo 2:

# Entrada: nums = [2,2,1,1,1,2,2]
#  Saída: 2


# Restrições:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
