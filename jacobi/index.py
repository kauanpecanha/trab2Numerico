import math
import matplotlib.pyplot as plt
import numpy as np

def Calc1(x2, x3, x4):
    return (1 / A[0][0]) * (A[0][4] - A[0][1] * x2 - A[0][2] * x3 - A[0][3] * x4)

def Calc2(x1, x3, x4):
    return (1 / A[1][1]) * (A[1][4] - A[1][0] * x1 - A[1][2] * x3 - A[1][3] * x4)

def Calc3(x1, x2, x4):
    return (1 / A[2][2]) * (A[2][4] - A[2][0] * x1 - A[2][1] * x2 - A[2][3] * x4)

def Calc4(x1, x2, x3):
    return (1 / A[3][3]) * (A[3][4] - A[3][0] * x1 - A[3][1] * x2 - A[3][2] * x3)

def CalcDiferenca(x_d, x_a):
    return(abs(x_d - x_a))
    

epsilon = float(input('Entre com E: '))

A = np.array(
    [
        [5, 3, -2, 1, -6],
        [1, -4, 2, 3, 10],
        [1, 2, -3, 1, -10],
        [2, 1, -2, 3, -7],
    ]
)

contador = 0
x = np.array([0, 0, 0, 0])

while(True):

    x1_a = x[0]
    x2_a = x[1]
    x3_a = x[2]
    x4_a = x[3]

    x1_d = Calc1(x2_a, x3_a, x4_a)
    x2_d = Calc2(x1_a, x3_a, x4_a)
    x3_d = Calc3(x1_a, x2_a, x4_a)
    x4_d = Calc4(x1_a, x2_a, x3_a)

    print(f'{x1_d:.2f}, {x2_d:.2f}, {x3_d:.2f}, {x4_d:.2f}')

    control = [0, 0, 0, 0]
    control[0] = CalcDiferenca(x1_d, x1_a)
    control[1] = CalcDiferenca(x2_d, x2_a)
    control[2] = CalcDiferenca(x3_d, x3_a)
    control[3] = CalcDiferenca(x4_d, x4_a)

    x = np.array([x1_d, x2_d, x3_d, x4_d])
    
    if(np.max(control) > epsilon):
        print(f'{np.max(control)} > {epsilon}. Continua na próxima iteração.')
        contador+=1
    else:
        print(f'{np.max(control)} < {epsilon}. Tolerância atingida.')
        print(f'Total de iterações: {contador+1}, e o vetor de resultados é: {x}')
        break