import matn
import math
import numpy as np
import multiprocessing as mp
import PySimpleGUI as sg
import time

seria_mas = []
eps_mas = []


# pie = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651


def func(x):
    return x ** 3 + 1   # интеграл на интервале от 0 до 2 равен 6


def thread_res(num, func_s):
    k = 0
    s = ''
    match func_s:
        case '1':
            s = 'вектора'
        case '2':
            s = 'интеграла'
    sg.one_line_progress_meter(f'Рассчет {s} {num}', k, 100, 'Идет рассчет вектора, ждите...', orientation='h')
    vc = []
    for i in range(4, 9):
        k += 10
        sg.one_line_progress_meter(f'Рассчет {s} {num}', k, 100, f'Идет рассчет вектора {num}, ждите...',
                                   orientation='h')
        if func_s == "matn.calc_pi":
            vc.append(matn.calc_pi(1, 2, 5, 10 ** i))
        elif func_s == "matn.calc_int":
            vc.append(matn.calc_int(0, 2, func, 10 ** i))
        # print(f"{i-3} ---", vc, sep=' ')
        k += 10
        sg.one_line_progress_meter(f'Рассчет {s} {num}', k, 100, f'Идет рассчет вектора {num}, ждите...',
                                   orientation='h')
    return np.array(vc)


def task_2(procs, func_s):
    processes = []
    for proc in range(procs):
        p = mp.Process(target=seria_mas.append(thread_res(proc + 1, func_s)))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    seria_1 = seria_mas[0]
    seria_2 = seria_mas[1]
    seria_3 = seria_mas[2]
    seria_4 = seria_mas[3]
    seria_5 = seria_mas[4]

    print(f"Вектор 1 - {seria_1}")
    print(f"Вектор 2 - {seria_2}")
    print(f"Вектор 3 - {seria_3}")
    print(f"Вектор 4 - {seria_4}")
    print(f"Вектор 5 - {seria_5}")


def task_3(func_s):
    for i in range(5):
        ser_all = 0
        eps_v = []
        for j in range(5):
            if func_s == "matn.calc_pi":
                eps_v.append(abs((seria_mas[i][j] - math.pi) / math.pi))
            elif func_s == "matn.calc_int":
                eps_v.append(abs((seria_mas[i][j] - 6) / 6))
            ser_all += seria_mas[j][i]
        eps_mas.append(np.array(eps_v))
        s_e = ser_all / 5
        if func_s == "matn.calc_pi":
            eps_s_e = abs((s_e - math.pi) / math.pi)
        elif func_s == "matn.calc_int":
            eps_s_e = abs((s_e - 6) / 6)
        print(f"-----------------\n"
              f"s_e{i + 4} = {s_e}\n"
              f"Eps_S_e{i + 4} = {eps_s_e}")

    eps_1 = eps_mas[0]
    eps_2 = eps_mas[1]
    eps_3 = eps_mas[2]
    eps_4 = eps_mas[3]
    eps_5 = eps_mas[4]
    print("--------------------------------------\n"
          "------------Погрешности:--------------\n"
          f"Для серии экспериментов 1 --- {eps_1}\n"
          f"Для серии экспериментов 2 --- {eps_2}\n"
          f"Для серии экспериментов 3 --- {eps_3}\n"
          f"Для серии экспериментов 4 --- {eps_4}\n"
          f"Для серии экспериментов 5 --- {eps_5}\n"
          "-------------------------------------")


if __name__ == '__main__':
    print("-----------Лабораторная-работа--1----------\n"
          "Выберите действие:\n"
          "Для вычисления числа pi --- 1\n"
          "Для вычисления интеграла --- 2")
    while True:
        try:
            func_s = int(input("Введите номер действия: "))
            if func_s != 1 or func_s != 2:
                print("Число не соответствует заданным параметрам. Попробуйте еще раз.")
                continue
            break
        except ValueError:
            pass
        print("Вы ввели что-то не то. Попробуйте еще раз")
    match func_s:
        case 1:
            start = time.time()
            task_2(5, 'matn.calc_pi')
            end = time.time()
            task_3('matn.calc_pi')
        case 2:
            start = time.time()
            task_2(5, 'matn.calc_int')
            end = time.time()
            task_3('matn.calc_int')
