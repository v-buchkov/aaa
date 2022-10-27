import numpy as np

LEARNING_RATE = 0.01
BETA = 0.25
MAX_ITERATIONS = 250
TOLERANCE = 0.000000001


def f(x: float, y: float) -> float:
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


def dfdx(x: float, y: float) -> float:
    return 2 * (x ** 2 + y - 11) * 2 * x + 2 * (x + y ** 2 - 7)


def dfdy(x: float, y: float) -> float:
    return 2 * (x ** 2 + y - 11) + 2 * (x + y ** 2 - 7) * 2 * y


def find_minima(x: float, y: float) -> tuple:

    alpha = LEARNING_RATE

    iter_num = 0
    dfdx_value, dfdy_value = np.inf, np.inf
    w_x, w_y = 0, 0

    alpha_decreaser = 1
    sign_value = [0, 0]

    while iter_num < MAX_ITERATIONS and np.linalg.norm([dfdx_value, dfdy_value]) > TOLERANCE:

        if not np.all(np.sign([dfdx_value, dfdy_value]) == sign_value):
            sign_value = np.sign([dfdx_value, dfdy_value])
            alpha_decreaser += 1
            alpha = alpha / alpha_decreaser

        dfdx_value = np.clip(dfdx(x, y), -100, 100)
        dfdy_value = np.clip(dfdy(x, y), -100, 100)

        w_x = w_x * BETA + dfdx_value * (1 - BETA)
        x = x - alpha * w_x

        w_y = w_y * BETA + dfdy_value * (1 - BETA)
        y = y - alpha * w_y

        iter_num += 1

    return round(x, 5), round(y, 5)


def solution():
    x_0, y_0 = map(float, input().split())
    minima_coordinates = find_minima(x_0, y_0)
    result = ' '.join(map(str, minima_coordinates))
    print(result)


solution()
