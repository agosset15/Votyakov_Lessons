def task_1():
    return print([2] * 3)

def task_2():
    return print([1] + [2] * 2)

def task_3():
    n = int(input("Введите число n: "))
    a = []
    for i in range(n):
        a.append(int(input("Введите число: ")))
    print(sum(a)//len(a))

def task_4():
    n = int(input("Введите число n: "))
    m = int(input("Введите число m: "))
    a = []
    for i in range(n):
        a.append(int(input("Введите число: ")))
    print(a[m])

def task_5():
    n = int(input("Введите число n: "))
    a = []
    for i in range(n):
        a.append(int(input("Введите число: ")))
    print(sum(a[::2]))

if __name__ == "__main__":
    task_1()
    task_2()
    task_3() # 4
    task_4() # 32
    task_5() # 6
