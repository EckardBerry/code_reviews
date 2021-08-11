
class Solution:
    def addTwoNumbers(self, l1, l2):
        string_1 = ''.join(map(str, l1))
        string_2 = ''.join(map(str, l2))
        solution = list(map(int, str(int(string_1) + int(string_2))))
        return solution[::-1]

problem = Solution()
print(problem.addTwoNumbers([2, 4, 3], [5, 6, 4]))
