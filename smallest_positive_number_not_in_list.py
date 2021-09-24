def solution(A):
    for i in range(1, abs(max(A))+1):
        if i not in A:
            return i
        elif (max(A)+1) == 0:
            return 1
    return (max(A)+1)



print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))