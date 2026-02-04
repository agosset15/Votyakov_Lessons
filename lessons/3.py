def task_1():
    return print("x % 2 != 0 or x % 5 != 0")

def task_2():
    return print("i 10")

def task_3():
    k = int(input("Введите K: "))
    n = int(input("Введите M: "))
    x = 0
    while k <= n:
        x += n % 2
        n -= 1
    return print(x)

def task_4():
    n = int(input("Введите N: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return print(factorial)

if __name__ == "__main__":
    task_1() # x % 2 != 0 or x % 5 != 0
    task_2() # i 10
    task_3() # 22223
    task_4() # 3628800