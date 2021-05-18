# Have the function FibonacciChecker(num) return the string yes if the number given is part of the Fibonacci sequence.
# This sequence is defined by: Fn = Fn-1 + Fn-2, which means to find Fn you add the previous two numbers up. The first
# two numbers are 0 and 1, then comes 1, 2, 3, 5 etc. If num is not in the Fibonacci sequence, return the string no.

def FibonacciChecker(num):
    fibonacci_sequence = [0, 1]
    for i in range(0, num):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    if num in fibonacci_sequence:
        return 'yes'
    else:
        return 'no'


print(FibonacciChecker(13))