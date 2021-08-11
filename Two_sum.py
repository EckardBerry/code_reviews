"""
def two_sum(some_list, target):
    from itertools import combinations
    combs = combinations(some_list, 2)
    for comb in combs:
        if sum(comb) == target:
            print(comb)



two_sum([3, 1, 5, 7, 5, 9], 10)
"""

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        from itertools import permutations as cm
        combos = list(cm(nums, 2))
        for combo in combos:
            if sum(combo) == target:
                new_string = f'[{nums.index(combo[0])}, {nums.index(combo[1])}]'
                break
        print(new_string)


problem = Solution()
problem.twoSum([2, 7, 11, 15], 9)
problem.twoSum([3, 2, 4], 6)