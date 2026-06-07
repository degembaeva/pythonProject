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


