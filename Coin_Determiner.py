
# Have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250, and return an
# integer output that will specify the least number of coins, that when added, equal the input integer.
# Coins are based on a system as follows: there are coins representing the integers 1, 5, 7, 9, and 11.
# So for example: if num is 16, then the output should be 2 because you can achieve the number 16 with the
# coins 9 and 7. If num is 25, then the output should be 3 because you can achieve 25 with either 11, 9, and 5
# coins or with 9, 9, and 7 coins.
"""
from itertools import combinations as cm
def CoinDeterminer(num):
    coin_list = [1, 5, 7, 9, 11]
    for i in range(1, num):
        combs = cm(coin_list, i)
        for comb in combs:
            if sum(comb) == num:
                return len(comb)
    else:
        return -1

print(CoinDeterminer(16))
print(CoinDeterminer(55))
"""
import math
def find_roots(a, b, c):
    sqrt_arg = b**2 - 4*a*c
    two_a = 2*a
    if sqrt_arg >= 0:
        x_1 = (-b + math.sqrt(sqrt_arg))/two_a
        x_2 = (-b - math.sqrt(sqrt_arg))/two_a
        return x_1, x_2
    return -b/two_a

print(find_roots(2, 10, 8))