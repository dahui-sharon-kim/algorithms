def fibonacci(n): # 최적 알고리즘으로, 고정된 크기의 메모리만 사용하므로 공간 복잡도가 O(1)
    p2, p1 = 0, 1 # 2개 전, 1개 전
    for i in range(n):
        p2, p1 = p1, p2 + p1
    return p2

print(fibonacci(40))