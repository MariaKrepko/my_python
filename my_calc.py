print('Введите два числа и действие между ними в формате: x,y,(plus,minus,multiply,divide, power) ')
x=int(input())
y=int(input())
c=input()
if c=='plus':
    print(x+y)
if c=='minus':
     print(x-y)
if c=='multiply':
     print(x*y)
if c=='power':
    print(pow(x,y))
if c=='divide':
    if y!=0:
        print(x/y)
    elif y==0:
        try:
            print(x/y) 
        except ZeroDivisionError:
            print('Ошибка деления')
