from random import randint
lst = [randint(-50, 50) for i in range(1000)]
print(lst)
count=0
m_n=min(lst)
m_x=max(lst)
index_min=lst.index(m_n)
index_max=lst.index(m_x)
if index_min < index_max:
    lst_2=lst[index_min:index_max+1]
    for i in lst_2:
        if i<0:
            count=count+1
    print("Кол-во отрицательных элементов между мин и макс:",count)
else:
     lst_3=lst[index_max:index_min+1]
     for i in lst_3:
         if i<0:
            count=count+1
     print("Кол-во отрицательных элементов между мин и макс:",count)
