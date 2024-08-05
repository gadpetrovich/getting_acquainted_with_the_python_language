var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

v1 = list(map(int, var1.split()))
v2 = [int(x) for x in var2.split()]
v3 = [int(x) for x in var3.split()]

s1 = set()
for i in range(v1[0]):
  s1.add(v2[i])
  
s2 = set()
for j in range(v1[1]):
  s2.add(v3[j])

s = sorted(s1.intersection(s2))
print(str.join(' ', map(str, list(s))))
