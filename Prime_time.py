def prime_time(num):
    result = list(map(lambda x: num if num % x == 0 else None, list(range(2, num))))
    if num in result or num == 1:
        return 'false'
    return 'true'


print(prime_time(2))