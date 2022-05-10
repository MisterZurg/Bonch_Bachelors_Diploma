'''
x=input("Введите число, до которого следует вести подсчёт: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break
'''

# Модифицированный while: Проверять наличие команды quit
while True:
    x=input("Введите число, до которого следует вести подсчёт: ")
    if x == 'q' or x == 'quit':
        break

    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
