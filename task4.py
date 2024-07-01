n = int(input())
m = int(input())
k = int(input())

value = k % m == 0 and n * m >= k

if value:
  print("yes")
else:
  print("no")
