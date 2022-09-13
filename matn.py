from random import *


def calc_pi(x0: float, y0: float, r0: float, exp_num: int):
    m = 0
    x_min = x0 - r0
    x_max = x0 + r0
    y_min = y0 - r0
    y_max = y0 + r0
    for i in range(1, exp_num):
        p = random()
        x = (x_max-x_min) * p + x_min
        p = random()
        y = (y_max - y_min) * p + y_min
        if (((x-x0)**2) + ((y-y0)**2)) < (r0**2):
            m += 1
    return 4 * m / exp_num


def calc_int(a, b, func, exp_num):
    m = 0
    x_min = a
    x_max = b
    y_min = 0
    y_max = func(b)
    for i in range(1, exp_num):
        p = random()
        x = (x_max - x_min) * p + x_min
        p = random()
        y = (y_max - y_min) * p + y_min
        if func(x) > y:
            m += 1
    return func(b)*(b-a)*m/exp_num
