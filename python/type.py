a: str = "1"
b: int = 1
def isOdd(a: int) -> bool:
  if a % 2:
    return True
  return False

print(isOdd(3))