def task_1():
    str_1 = input("Введите первую строку: ")
    str_2 = input("Введите вторую строку: ")
    str_3 = input("Введите третью строку: ")
    return print(str_1 + str_2 + str_3)

def task_2():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    answer = 2**8 * a ** 8 - 2**4 * a**4 + 2**2 * a**2 - 2 * b + 0.5 * b**0.5 + (a * b)**(b + a) / 2
    return print(answer)

def task_3():
    return print("23!")

def task_4():
    return print("(123 + 456 - 789) % 10 = 0")

def task_5():
    digit = int(input("Введите число: "))
    print(digit + 1, digit - 1, sep="")

def task_6():
    centimeters = int(input("Введите длину в сантиметрах: "))
    print(centimeters / 100_000)


if __name__ == "__main__":
    task_1() # Программирование после школы!
    task_2() # 32134205104895.5
    task_3() # 23!
    task_4() # (123 + 456 - 789) % 10 = 0
    task_5() # 2523
    task_6() # 1234.56789