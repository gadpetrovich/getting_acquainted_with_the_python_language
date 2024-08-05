stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
glasnie = 'аеёиоуыэюя'

def all_same(list):
  value = True
  for i in range(len(list) - 1):
    if (list[i] != list[i + 1]):
      value = False
      break
  return value

list1 = stroka.split()
if len(list1) < 2:
  print('Количество фраз должно быть больше одной!')
else:
  list2 = [len(list(c for c in line if c in glasnie)) for line in list1]
  if (all_same(list2)):
    print('Парам пам-пам')
  else:
    print('Пам парам')

#print(list2)