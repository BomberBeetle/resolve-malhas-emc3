import numpy as np

n = int(input("Digite o número de malhas: "))

tabela_coef= np.zeros(shape=(n, n), dtype=np.single)
tabela_ord = np.zeros(shape=(n), dtype=np.single)

for i in range(n):
    
    tabela_ord[i] = float(input("Digite a tensão da malha {}: ".format(i+1)))
    tabela_coef[i][i] = float(input("Digite a resistência total (não compartilhada com outras malhas) da malha {}: ".format(i+1)))
    for j in range(n-i-1):
        nres = float(input("Digite a resistência compartilhada entre as malhas {} e {}: ".format(i+1, j+2+i)))
        tabela_coef[i][i] += nres
        tabela_coef[i][j+1+i] += nres
        tabela_coef[j+1+i][i] += nres
        tabela_coef[j+1+i][j+1+i] += nres

res = np.linalg.solve(tabela_coef, tabela_ord)

#TODO: Ver como faz a equação direitinho... só ver isso que o numpy resolve direto.

for idx, val in enumerate(res, start=1):
    print("Corrente da malha {}: {}".format(idx, val))