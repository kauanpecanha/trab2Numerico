import math
import matplotlib.pyplot as plt
import numpy as np

epislon = 0.000000000000001
tol = epislon + 1  # Inicializar tol com um valor maior que epislon
w = 1.19  # fator de relaxação
inter = 0  # definindo número de iterações

# Definindo a matriz ============================================
A = np.array(
    [
        [5, 3, -2, 1, -6],
        [1, -4, 2, 3, 10],
        [1, 2, -3, 1, -10],
        [2, 1, -2, 3, -7],
    ]
)

xk = np.array([0.0, 0.0, 0.0, 0.0])  # definindo x0

# Cálculo dos Residuos ============================================
def R1(x1, x2, x3, x4):
    return A[0, 4] - A[0, 0] * x1 - A[0, 1] * x2 - A[0, 2] * x3 - A[0, 3] * x4

def R2(x1, x2, x3, x4):
    return A[1, 4] - A[1, 0] * x1 - A[1, 1] * x2 - A[1, 2] * x3 - A[1, 3] * x4

def R3(x1, x2, x3, x4):
    return A[2, 4] - A[2, 0] * x1 - A[2, 1] * x2 - A[2, 2] * x3 - A[2, 3] * x4

def R4(x1, x2, x3, x4):
    return A[3, 4] - A[3, 0] * x1 - A[3, 1] * x2 - A[3, 2] * x3 - A[3, 3] * x4

# Cálculo dos X ============================================
def X1(w, R1, x1):
    return x1 + ((w / A[0, 0]) * R1)

def X2(w, R2, x2):
    return x2 + ((w / A[1, 1]) * R2)

def X3(w, R3, x3):
    return x3 + ((w / A[2, 2]) * R3)

def X4(w, R4, x4):
    return x4 + ((w / A[3, 3]) * R4)

# Calculando a tolerancia ============================================
def CalcTol(y, xk):
    maior_y = np.max(np.abs(y))
    maior_xk = np.max(np.abs(xk))

    if maior_y != 0:
        return maior_y / maior_xk
    else:
        return 0.0

# Loop até atingir critério de parada ==========================================
while tol > epislon:
    inter += 1

    # Salvando xk
    xk_old = np.copy(xk)

    # Cálculo dos resíduos e Atualização dos valores de xk usando o método SOR
    Rnovo1 = R1(xk[0], xk[1], xk[2], xk[3])
    xk[0] = X1(w, Rnovo1, xk[0])

    Rnovo2 = R2(xk[0], xk[1], xk[2], xk[3])
    xk[1] = X2(w, Rnovo2, xk[1])

    Rnovo3 = R3(xk[0], xk[1], xk[2], xk[3])
    xk[2] = X3(w, Rnovo3, xk[2])

    Rnovo4 = R4(xk[0], xk[1], xk[2], xk[3])
    xk[3] = X4(w, Rnovo4, xk[3])

    print(f'Valor do Residuo 1 = {Rnovo1}')
    print(f'Valor do Residuo 2 = {Rnovo2}')
    print(f'Valor do Residuo 3 = {Rnovo3}')
    print(f'Valor do Residuo 4 = {Rnovo4}')

    temporaria = xk - xk_old

    # Cálculo da nova tolerância
    tol = CalcTol(temporaria, xk)

    print(f'Tolerancia = {tol}')
    print(f'Iterações = {inter}')

print('-'*100)
print(f'\n\n\nMÉTODO DE SOR\nO resultado final pode ser visualizado abaixo:\n\n'
      +f'\nResíduos:\n\n'
      +f'\nR1={Rnovo1:.15f}\nR2={Rnovo2:.15f}\nR3={Rnovo3:.15f}\nR4={Rnovo4:.15f}\n'
      +f'\n\nRaízes:\n\n'
      +f'\nX1={xk[0]}\nX2={xk[1]}\nX3={xk[2]}\nX4={xk[3]}'
      +f'\n\nObtidos após {inter} iterações.\n\n'
      f'\n\nFator de relaxação: {w}')