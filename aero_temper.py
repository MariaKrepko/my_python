temp = {}

with open("temper.txt", 'r') as file:
    contents = file.read()

for temp in contents.split():
    tempList.append(float(temp))


print('Максимальная температура: ', max(temp),'\nМинимальная температура: ', min(temp),
      '\nСредняя температура: ', sum(temp)/len(temp),'\nКоличество уникальных температур: ', len(set(tempList))
      )
