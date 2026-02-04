def task_1(str_1: str, str_2: str, str_3: str):
    return print(str_1 + str_2 + str_3)

def task_2(a: int, b: int):
    answer = 2**8 * a ** 8 - 2**4 * a**4 + 2**2 * a**2 - 2 * b + 0.5 * b**0.5 + (a * b)**(b + a) / 2
    return print(answer)

def task_3():
    return print("23!")

def task_4():
    return print("(123 + 456 - 789) % 10 = 0")

def task_5(digit: int):
    print(digit + 1, digit - 1, sep="")

def task_6(centimeters: int):
    print(centimeters / 100_000)


if __name__ == "__main__":
    task_1('Программирование ', 'после ', 'школы!')
    task_2(2, 9)
    task_3()
    task_4()
    task_5(24)
    task_6(123456789)