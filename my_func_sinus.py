import math
X=float(input('Введите значение Х '))
if 0.2<=X<=0.9:
    z=math.sin(X)
    print('f=',z)
else:
    print('f=1')
