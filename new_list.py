#Задача а
lst=[2,4,9,16,25]
for i in range(len(lst)):
   lst[i]=lst[i]*lst[i]
print(lst)

#Задача б
lst=[2,4,9,16,25]
print(list(map((lambda i:i**2),lst)))
         
#Задача в
s = [2, 4, 9, 16, 25]
print([i**2 for i in s])
