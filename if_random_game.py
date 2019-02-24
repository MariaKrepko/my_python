import random
print("Дмитрий Юрьевич, введите число от 1 до 4")
a=int(input())
b=random.randint(1,4)
if a==b:
    print("Победа")
else:
    if a>b:
        print("Введённое вами число больше псевдорандомного") 
    else:
         print("Введённое вами число меньше псевдорандомного")
