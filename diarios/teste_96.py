class Solution:
<<<<<<< HEAD
        def frequencySort(self, A):
            count = collections.Counter(A)
            return sorted(A, key=lambda x: (count[x], -x))
=======
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted([[height, name] for height, name in zip(heights, names)], reverse=True)]
>>>>>>> 99850e0cf2d0c826889f33cb0c02a20952380062
