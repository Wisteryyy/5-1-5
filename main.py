a=str(input("Введите строку: "))
b=[]
for i in range(len(a)):
    if a[i] == 'е':
        b.append(i)
if b:
    print(f"Индексы символа 'e' в строке: {b}")
else:
    print("Символ 'e' отсутствует в строке.")