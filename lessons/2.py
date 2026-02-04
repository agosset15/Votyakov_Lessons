def task_1():
    print('True')

def task_2():
    password = input('Введите пароль: ')
    password_confirm = input('Подтвердите пароль: ')
    if password == password_confirm:
        return print('True')
    return print('False')

def task_3():
    digits = []
    for _ in range(4):
        digits.append(int(input('Введите число: ')))
    return print(min(digits))

def task_4():
    digits = []
    for _ in range(4):
        digits.append(int(input('Введите число: ')))
    return print(max(digits))

def is_triangle(a, b, c):
    return (a < (b + c)) and (b < (a + c)) and (c < (a + b))

def task_5():
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    c = int(input('Введите число: '))
    return print(is_triangle(a, b, c))

def task_6():
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    c = int(input('Введите число: '))
    if a != b != c and is_triangle(a, b, c):
        return print('Разносторонний')
    if a == b == c:
        return print('Равносторонний')
    return print('Вырожденный')

def task_7():
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    c = int(input('Введите число: '))
    d = int(input('Введите число: '))
    if not (a <= b) or not (c <= d):
         return print('Ошибка!')
    section_1 = set(range(a, b + 1))
    section_2 = set(range(c, d + 1))
    return print(len(section_1.intersection(section_2)))

if __name__ == '__main__':
    task_1()
    task_2() # False
    task_3() # 5
    task_4() # 30
    task_5() # False
    task_6() # Вырожденный
    task_7() # 7