def factorial(n):
    if n == 0: # 기저 조건
        return 1
    return n * factorial(n-1) # 재귀 호출 (자기 자신을 호출)

print(factorial(5))