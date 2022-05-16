import numpy as np

n = int(input("Digite o número de malhas: "))

tabela_coef= np.zeros(shape=(n, n), dtype=np.float_)
tabela_ord = np.zeros(shape=(n), dtype=np.float_)

for i in range(n):
    
    tabela_ord[i] = 0-float(input("Digite a tensão da malha {}: ".format(i+1)))

for i in range(n):

    tabela_coef[i][i] += float(input("Digite a resistência total (não compartilhada com outras malhas) da malha {}: ".format(i+1)))
    for j in range(n-i-1):
        nres = float(input("Digite a resistência compartilhada entre as malhas {} e {}: ".format(i+1, j+2+i)))

        if(tabela_ord[i] > tabela_ord[j]):
            tabela_coef[i][i] -= nres
            tabela_coef[i][j+1+i] += nres
            tabela_coef[j+1+i][i] += nres
            tabela_coef[j+1+i][j+1+i] -= nres
        else:
            tabela_coef[i][i] += nres
            tabela_coef[i][j+1+i] -= nres
            tabela_coef[j+1+i][i] -= nres
            tabela_coef[j+1+i][j+1+i] += nres
        

res = np.linalg.solve(tabela_coef, tabela_ord)

for idx, val in enumerate(res, start=1):
    print("Corrente da malha {}: {}".format(idx, val))