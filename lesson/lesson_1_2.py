# Тема: Управляющие конструкции, ветвление, циклы
# недопускать лишнего отступа в начале строки (табуляции, пробелы)

a = 4
b = 0
 # Условлые операторы нужны когда мы хотим выполнить определенный код только при некоторым условии
print("Start of program")

if a > b:
    print("a > 0")
elif a > -5:
    print("-5 < a <= 0")
else:
    print("a <= -5")

print("End of program")

#Условные операторы
c = 4
d = 0
flag = True
flag2 = False

print(flag)
e = c > d
print(e)

print(c == 4) #сравнить на равно
print(c != d) #сравнить на не равно
print(c < d)
print(c >= d)
print(flag == flag2)

#логические операторы
print(not flag) #not - отрицает
print(not c < d) #not - делает обратно
print(c > d and c > 2) #and - оба условия должны быть true
print(c < d and c > 2)
print(c != d or c < d )#or - проверяет хотя бы одно условие true
print(c == d or c < d) #or - false false равно false

print( c > d or ((not c == d) and c > 0))
#самый высокий приоритет имеет - NOT
#следующий приоритет - AND
#самый низкий приоритет имеет - OR

#если OR в самом начале истина то сразу понятно что будет истина
n = c > d or d > 10

#анологично ANDесли первая часть false то будет false
m = c < 0 and d != 1

#Полезно также знать про тернарный оператор, он позволяет
# в компактной форме задать переменную в зависимости от условия

v = c if c > d else d

if c > d:
    v = c
else: v = d

# Циклы - FOR, для последовательности чисел
#(старт включительно, конец не включительно, шаг +1 значение по умолчанию)
for i in range(1, 10, 1):
    print(i)
print("END")

#от нуля до десяти будет выходить
for i in range(10):
    print(i)
print("END")

# Циклы - FOR, для последовательности символов

for i in "abc123":
    print(i)

# Циклы - FOR, с continue
for i in range(10):
    if i == 4:
        continue #пропустим если числа равна 4
    print(i)
print("END")

# Циклы - FOR, с break
for i in range(10):
    if i == 4:
        break #можем полностью остановить цикл если числа равна 4
    print(i)
print("END")

# Циклы - WHILE, выполняет код пока выполнены некоторые условия

k = 0
while k < 10:
    print(k)
    k += 1
    if k > 5:
        break
print("end")

#пустая строка
print(bool(""), bool("Abc"))

#проверяет data является пустой строкой или нет, если пустое то завершает цикл
data = input()
while data:
    print("Entered:", data)
    data = input()


while data := input():
    print("Entered: ", data)
