def print_operation_table(operation, num_rows=9, num_columns=9):
  if (num_rows < 2):
    print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    return
  
  for y in range(1, num_rows + 1):
    print(str.join(' ', [str(operation(y, x)) for x in range(1, num_columns + 1)]))
  
print_operation_table(lambda x, y: x * y)