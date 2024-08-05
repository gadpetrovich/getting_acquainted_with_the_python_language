list_1 = [1, 2, 3, 4, 5]
k = 6

nearest_value = list_1[0]
for i in list_1:
  if (abs(k - i) < abs(k - nearest_value)):
    nearest_value = i

print(nearest_value)