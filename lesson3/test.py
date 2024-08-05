# list1 = [1,1,2,3,5,6]
# #print(len(set(list1)))

# #сдвинуть на k вправо
# k = 2
# for i in range(k):
#   list1.insert(0, list1.pop())


# print(list1)


#----

# list1 = [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
# print(set(map(lambda x: list(x.values())[0], list1)))

#---

list1 = [0,-1,5,2,3]

counter = 0
for i in range(len(list1) - 1):
  if list1[i + 1] > list1[i]:
    counter += 1
print(counter)