value = int(input())

v1 = value // 100
v2 = value // 10 - v1 * 10
v3 = value - v1 * 100 - v2 * 10

print(v1 + v2 + v3)