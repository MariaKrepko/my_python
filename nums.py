text = '''В разные эпохи и у разных народов число Пи имело разное значение.
Например, в Древнем Египте оно равнялось 3.1604 у индусов оно приобрело
значение 3.162 китайцы пользовались числом, равным 3.1459
Буквенное обозначение число Пи получило только в 1706 году – оно происходит
от начальных букв двух греческих слов, означающих окружность и периметр.
Буквой π число наделил математик Джонс, а прочно вошла в математику она
уже в 1737 году.'''
k=[]
sum_=0
count=0
maxi=0
for i in range(len(text)):
    if text[i].isdigit():
        k.append(text[i])
        sum_=sum_+int(text[i])
        count+=1
        if int(text[i])>maxi:
            maxi=int(text[i])

print(k)
print("Количество:",count)
print("Сумма:",sum_)
print("Наибольший:",maxi)