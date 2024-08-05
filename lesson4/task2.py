arr = [5, 8, 6, 4, 9, 2, 7, 3]

#arr2 = [x + arr[i - 1] + arr[(i + 1) % len(arr)] for i, x in enumerate(arr)]
#print(max(arr2))

d = {}

for i, x in enumerate(arr):
  d[i] = x + arr[i - 1] + arr[(i + 1) % len(arr)]

print(max(d.values()))
