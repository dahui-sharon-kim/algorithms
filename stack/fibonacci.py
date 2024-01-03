# 반복 알고리즘 (Iterative implementation)

def fibonacci(n):
    total = 0
    stack = [n]
    while stack:
        n = stack.pop()
        if n < 2:
            total += n
        else:
            stack.append(n - 1) # breaks down the problem into smaller subproblems
            stack.append(n - 2)
    return total

print(fibonacci(2))
