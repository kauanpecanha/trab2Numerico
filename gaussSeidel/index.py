import math
import matplotlib.pyplot as plt
import numpy as np

epislon = float(input('Entre com o valor E: '))
tol = epislon + 1  # Inicializar tol com um valor maior que epislon

A = np.array(
    [
        [5, 3, -2, 1, -6],
        [1, -4, 2, 3, 10],
        [1, 2, -3, 1, -10],
        [2, 1, -2, 3, -7],
    ]
)

x1 = (A[0][4] / A[0][0])
x2 = (A[1][4] / A[1][1])
x3 = (A[2][4] / A[2][2])
x4 = (A[3][4] / A[3][3])

x = np.array([x1, x2, x3, x4])

xk1 = (A[0][4] / A[0][0])
xk2 = (A[1][4] / A[1][1])
xk3 = (A[2][4] / A[2][2])
xk4 = (A[3][4] / A[3][3])

xk = np.array([xk1, xk2, xk3, xk4])
y = np.array([0.0, 0.0, 0.0, 0.0])

def Calc1(x2, x3, x4):
    return (1 / A[0][0]) * (A[0][4] - A[0][1] * x2 - A[0][2] * x3 - A[0][3] * x4)

def Calc2(x1, x3, x4):
    return (1 / A[1][1]) * (A[1][4] - A[1][0] * x1 - A[1][2] * x3 - A[1][3] * x4)

def Calc3(x1, x2, x4):
    return (1 / A[2][2]) * (A[2][4] - A[2][0] * x1 - A[2][1] * x2 - A[2][3] * x4)

def Calc4(x1, x2, x3):
    return (1 / A[3][3]) * (A[3][4] - A[3][0] * x1 - A[3][1] * x2 - A[3][2] * x3)

def CalcTol(y, xk):
    maior_y = np.max(np.abs(y))
    maior_xk = np.max(np.abs(xk))

    if maior_y != 0:
        return maior_xk / maior_y
    else:
        return 0.0

inter = 0

while tol > epislon:
    inter = inter + 1

    print(f'Valor de X1= {Calc1(x2, x3, x4):.8f}')
    print(f'Valor de X2= {Calc2(x1, x3, x4):.8f}')
    print(f'Valor de X3= {Calc3(x1, x2, x4):.8f}')
    print(f'Valor de X4= {Calc4(x1, x2, x3):.8f}')

    y = np.array([Calc1(x2, x3, x4), Calc2(x1, x3, x4), Calc3(x1, x2, x4), Calc4(x1, x2, x3)])

    temporaria = y - xk
    tol = CalcTol(y, temporaria)

    x1 = Calc1(x2, x3, x4)
    x2 = Calc2(x1, x3, x4)
    x3 = Calc3(x1, x2, x4)
    x4 = Calc4(x1, x2, x3)

    xk = np.array([x1, x2, x3, x4])

    print(f'Tolerancia= {tol:.8f}')
    print(f'Iterações= {inter}')

    y = np.array([Calc1(x2, x3, x4), Calc2(x1, x3, x4), Calc3(x1, x2, x4), Calc4(x1, x2, x3)])
