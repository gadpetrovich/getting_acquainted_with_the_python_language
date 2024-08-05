def sum(a: int, b: int) -> int:
  if b == 0:
    return 0
  if a == 0:
    return sum(0, b - 1) + 1
  return sum(a - 1, b) + 1

a = 3
b = 5
print(sum(a, b))