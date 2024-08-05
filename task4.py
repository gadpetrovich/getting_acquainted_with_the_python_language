n = 2
m = 6
k = 10

value = (k % m == 0 or k % n == 0) and n * m >= k

if value:
  print("yes")
else:
  print("no")
