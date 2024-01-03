def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__": # checks whether the script is being run as the main program and not being imported as a module in another script
    for n in range(32):
        print(fibonacci(n), end=", ")