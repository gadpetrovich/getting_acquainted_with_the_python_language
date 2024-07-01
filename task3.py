value = int(input())

v1_1 = value // 100000
v1_2 = (value // 10000) % 10
v1_3 = (value // 1000) % 10
v2_1 = (value // 100) % 10
v2_2 = (value // 10) % 10
v2_3 = value % 10

is_happy = v1_1 + v1_2 + v1_3 == v2_1 + v2_2 + v2_3

if is_happy:
  print("yes")
else:
  print("no")