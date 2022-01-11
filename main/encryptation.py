#Resolvendo o algoritmo:
#https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true

s = "if man was meant to stay on the ground god would have given us roots"
lenght = len(s.replace(" ", ""))

import math

linhas = int(math.sqrt(lenght))
colunas = linhas + 1

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(0)
    matriz.append(1)

#exibindo matriz
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j])
#     print()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      print(matriz[i][j], end='  ')
    print()


